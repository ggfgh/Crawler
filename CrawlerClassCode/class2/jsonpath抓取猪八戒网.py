import requests
import pprint
import jsonpath
import json
import re
from bs4 import BeautifulSoup 
#https://jinshi.zbj.com
url = 'https://jinshi.zbj.com/api/unwanted/index2021/QftInfoService/getQftSearchInfo'
key_word = input('[*] 想要查询的服务:')
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
       
        "Referer":'https://taiyuan.zbj.com/search/f/?kw={keyword}'
    }

para = {
         'searchType': 1,
         'catType': 2,
         'cityId': 3803,
         'keyword':key_word,
         'currentPage':2,
         'size': 32,
     }


resp = requests.get(url,headers=headers,params=para)
json_data = resp.json()
#pprint.pprint(json_data)

#解析想要的数据
name_list = jsonpath.jsonpath(json_data,'$..brandName')
title_list = jsonpath.jsonpath(json_data,'$..title')
price_list = jsonpath.jsonpath(json_data,'$..price')
provinceName_list = jsonpath.jsonpath(json_data,'$..provinceName')
title_list = jsonpath.jsonpath(json_data,'$..title')
cityName_list = jsonpath.jsonpath(json_data,'$..cityName')

title_result_list = []
#处理title中的标签
for title in title_list:
    soup = BeautifulSoup(title,"html.parser")
    result = soup.text
    title_result_list.append(result)
#print(title_result_list)

#对应元素输出
a = zip(name_list,title_result_list,price_list,provinceName_list,cityName_list)
for i in a:
     print(i)
