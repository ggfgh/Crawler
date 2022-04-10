import requests
from bs4 import BeautifulSoup

url = 'http://www.bjtzh.gov.cn/bjtz/home/jrcj/index.shtml'
resp = requests.get(url)
resp.encoding = 'utf-8'

page = BeautifulSoup(resp.text,"html.parser")
#print(page)
table = page.find("table") #后面可以加特征 attr={"class":"hq_table"}
#print(table)
#每一行的内容,除去表头
trs = table.find_all('tr')[7:]
for tr in trs:
    tds = tr.find_all('td')
    name = tds[0].text #拿到被标签标记的内容
    card = tds[1].text
    high = tds[2].text
    avg = tds[3].text
    print(name, card, high, avg)