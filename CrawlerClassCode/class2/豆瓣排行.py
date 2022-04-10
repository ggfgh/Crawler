import requests
import re

url = 'https://movie.douban.com/chart'

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
}

resp = requests.get(url,headers=headers)
page_content = resp.text

#解析数据
expression =r'<tr class="item">.*? title="(?P<name>.*?)">.*? <p class="pl">(?P<year>.*?) .*?<span class="rating_nums">(?P<score>.*?)</span>.*?<span class="pl">(?P<num>.*?)</span>'
obj = re.compile(expression,re.S)

#匹配数据
result = obj.finditer(page_content)
for i in result:
    print(i.group("name"))
    print(i.group("year"))
    print(i.group("score"))
    print(i.group("num"))
  

