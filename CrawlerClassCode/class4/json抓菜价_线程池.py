import bs4
import requests
import json
import csv
import time
from concurrent.futures import ThreadPoolExecutor
import pymysql

def insert(data):
    conn = pymysql.connect(host='10.10.10.139',user='root',password='root',database='spinder_data',charset="utf8")

    cursor = conn.cursor()

    sql = 'insert into caijia(c_name,l_price,avg_price,type,des,date) values(%s,%s,%s,%s,%s,%s)'

    try:
        cursor.execute(sql,data)
        conn.commit()
    except Exception as e:
        print("插入数据失败:",e)
        conn.rollback() #回退

    cursor.close()

    conn.close()

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
            
            insert([name, low, avg, prodCat, place, date])
            print([name, low, avg, prodCat, place, date])
            #csvWrite.writerow([name, low, avg, prodCat, place, date])

if __name__ == '__main__':
    start = time.time()
    try:
        
        # for page in range(1,200):
        #     download_one_page(page)
        with ThreadPoolExecutor(100) as t:
            for i in range(5000,5600):
                 t.submit(download_one_page,i)

    except Exception as e:
        print("ERROR:",e)
    
    end = time.time()
    
    print("下载完毕,总用时 %d s" %(end - start))