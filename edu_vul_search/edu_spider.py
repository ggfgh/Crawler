import requests
import time
from lxml import etree
import sys
from concurrent.futures import ThreadPoolExecutor

def getInfo(page):
    print('提取 -> %s 页' %page)
    url = f'https://src.sjtu.edu.cn/list/?page={page}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}

    resp = requests.get(url,headers=headers,timeout=5)
    soup = etree.HTML(resp.text)
    results = soup.xpath('//td[@class=""]/a/text()')
    results = '\n'.join(results)
    results = results.split()
    for result in results:
        print(result)
        with open('eduVuln.txt','a',encoding='gbk') as f:
            f.write(result+'\n')
            time.sleep(0.1)

if __name__ == '__main__':
    page = input('pageCount:')
    threads = int(input('threads:'))
    
    start = time.time()
    with ThreadPoolExecutor(threads) as t:
        for idx in range(1,int(page)+1):
            t.submit(getInfo,idx)
    end = time.time()
    print('cost time: %s s' %(end - start))
