import requests
import re

domain = 'https://dy.dytt8.net/'

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

resp = requests.get(domain,headers=headers,verify=False)
#由于网页是GBK编码的，所以我们进行gbk编码
resp.encoding = 'gbk'
#print(resp.text)

child_href_list = []
obj1 = re.compile(r"手机浏览,推荐下载本站app,绿色小巧,简单实用！详情请点击.*?<tr>(?P<ul>.*?)</ul>",re.S)
obj2 = re.compile(r"最新电影下载.*?<a href='(?P<href>.*?)'")
obj3 = re.compile(r'◎片　　名　(?P<movie>.*?)<br />.*?href="(?P<download>.*?)"')

result1 = obj1.finditer(resp.text)
for it in result1:
        ul = it.group('ul')
        #提取子页面链接
        result2 = obj2.finditer(ul)
        for itt in result2:
                child_href = domain + itt.group('href').strip('/') #strip 去掉前面的/
                #将child_href放入child_href_list列表中
                child_href_list.append(child_href)
                #print(itt.group('href'))

#提取子页面的信息
for href in child_href_list:
        child_resp = requests.get(href,verify=False)
        child_resp.encoding = 'gbk'
        #print(child_resp.text)
        result3 = obj3.search(child_resp.text)
        print(result3.group("movie"))
        print(result3.group("download"))






