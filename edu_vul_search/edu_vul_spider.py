# -*- coding: utf-8 -*-
# @Time : 2022-4-11
# @Author : YaoW
# @Email: comedyyou@163.com
# @File: edu_vul_spider.py
# @Software: VS Code
import requests
import time
from lxml import etree
import sys
from concurrent.futures import ThreadPoolExecutor
from argparse import ArgumentParser

arg = ArgumentParser(description='baidu_url_collection')
arg.add_argument('keyword',help='关键字')
arg.add_argument('-p', '--page', help='page count', dest='pagecount', type=int,default=30)
arg.add_argument('-t', '--thread', help='the thread_count', dest='thread_count', type=int, default=10)
arg.add_argument('-o', '--outfile', help='the file save result', dest='outfile', default='eduVul.txt')
arg.add_argument('-n','--no-request',help='1:gather info, 0:do not gather info',dest='sign',type=int,default=1)
option = arg.parse_args()

def get_vuln_info(page):
    """
    漏洞信息收集模块
    """
    url = f'https://src.sjtu.edu.cn/list/?page={option.pagecount}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}

    resp = requests.get(url,headers=headers,timeout=5)
    soup = etree.HTML(resp.text)
    results = soup.xpath('//tr[@class="row"]/td[2]/a/text()')
    results = '\n'.join(results)
    results = results.split()
    
    for result in results:
        print(result)
        with open(option.outfile,'a',encoding='utf-8') as f:
            f.write(result+'\n')
            time.sleep(0.1)

def checkVul(keyword):
    """
    指定特定的高校，匹配其漏洞信息
    """
    print('-' * 20 + ' check vul information ' + '-' * 20)
    with open(option.outfile,'rb') as f:
        for line in f.readlines():
            try:
                line = line.decode('utf-8')
                line = line.replace('\n', '')
                if keyword in line:
                    print(line)
                    with open('target.txt','a',encoding='utf-8') as f:
                        f.write(line)
            except:
                continue

def main():
    if(option.sign == 1):
        with ThreadPoolExecutor(option.thread_count) as t:
            for i in range(1,int(option.pagecount)+1):
                t.submit(get_vuln_info,i)
        checkVul(option.keyword)
    
    else:
        checkVul(option.keyword)

if __name__ == '__main__':
    start = time.time()
    main()    
    end = time.time()
    print('cost time: %s s' %(end - start))
