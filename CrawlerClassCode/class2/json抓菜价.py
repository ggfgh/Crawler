import bs4
import requests
import json
import csv
import time
from concurrent.futures import ThreadPoolExecutor
import connect_mysql

def download_one_page(page):
    url = 'http://xinfadi.com.cn/getPriceData.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "http://xinfadi.com.cn/priceDetail.html",
    }

    #去掉文本中的\\和/
    #txt = (item.replace("\\",'').replace("/",'') for item in txt)
    #print(list(txt))

    #每次获取的条目
    limit = 20

    #页面
    current = page

    data = {
        'limit':limit,
        'current':current
    }

    f = open("蔬菜.csv","a+",newline='',encoding='utf-8')
    csvWrite = csv.writer(f)

    resp = requests.post(url,data=data)
    dic_json = json.loads(resp.text)
    #print(dic_json)
    for item in dic_json['list']:
            name = item['prodName']
            low = item['lowPrice']
            avg = item['avgPrice']
            prodCat = item['prodCat']
            place = item['place']
            date = item['pubDate']
            connect_mysql.insert(prodName, lowPrice, avgPrice, prodCat,place,pubDate)
            print(name, low, avg, prodCat, place, date)
            csvWrite.writerow([name, low, avg, prodCat, place, date])

if __name__ == '__main__':
    start = time.time()
    try:
        
        # for page in range(1,200):
        #     download_one_page(page)
        with ThreadPoolExecutor(1000) as t:
            for i in range(1,101):
                 t.submit(download_one_page,i)

    except:
        pass
    end = time.time()
    print("下载完毕,总用时 %d s" %(end - start))