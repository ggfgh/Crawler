import requests
from lxml import etree
from urllib import parse
import csv

url = 'https://search.jd.com/Search'
keyword = input("[*] 你想查询的书籍(类型):")
start = int(input("[*]start page:"))
end = int(input("[*]end page:"))

#创建保存数据的文件
f = open("jd_product.csv","w",encoding='gbk')
csvWrite = csv.writer(f)

for page in range(start,end+1):
        para = {
            "keyword": keyword,
            "page": page,
        }
        #参数url编码
        text = parse.urlencode(para)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
        }
        response = requests.get(url,headers=headers,params=text)

        #解析
        html = etree.HTML(response.text)

        #拿到每个商品的li
        lis = html.xpath("/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li")
        
        #从每本书的li中进行解析
        for li in lis:
                price = li.xpath("./div/div[2]/strong/i/text()")
                title = li.xpath("./div/div[3]/a/em//text()") #//text()获取子节点的所有内容
                img_src = li.xpath("./div/div[1]/a/img/@data-lazy-img")
                info = li.xpath("./div/div[7]/i[1]/text()") #是否自营
                
                #取出列表中的值
                title_str = ''.join(title)
                price_str = '￥' + ''.join(price)
                info_str  = ''.join(info)
                
                csvWrite.writerow([title_str,info_str,price_str])
                print(title_str,info_str,price_str)

print('[*] done')
        


