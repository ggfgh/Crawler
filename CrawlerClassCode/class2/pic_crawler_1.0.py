import requests
from bs4 import BeautifulSoup
import re
import time

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
}

#定义一些全局变量
total         = 0
last_img_name = ''


start = int(input("开始爬取图片的页数："))
end = int(input("终止爬取图片的页数："))

#设置爬取图片页数
for i in range(start,end+1):
    domain = 'https://699pic.com/photo-0-0-{0}.html'.format(i)
    resp = requests.get(domain,headers=headers)
    print('current url:',domain)
    resp.encoding = 'utf-8'
    #print(resp.text)

    #bs4处理获取获取图片子页面url
    str_href = ''
    main_page = BeautifulSoup(resp.text,"html.parser")
    alist = main_page.find("div",class_="imgshow clearfix").find_all("a")

    #获取a标签中的href
    for a in alist:
        href = a.get('href')
        str_href += str(href)

    #正则处理获取有效的href
    obj = re.compile(r"//(?P<pic_href>.*?).html",re.S)
    child_href_list = []
    result = obj.finditer(str_href)

    for href in result:
        child_href = 'https://' + href.group("pic_href") + '.html'
        #print(child_href)
        child_href_list.append(child_href)

    for child_href in child_href_list:
        
        child_resp = requests.get(child_href,headers=headers)
        child_resp.encoding = 'utf-8'
        #从子页面拿到图片下载链接
        child_page = BeautifulSoup(child_resp.text,"html.parser")
        div = child_page.find("div",class_="photo-img-block")
        img_a = div.find('a')
        
        src = 'https:' + img_a.get('href')
        #下载图片
        img_resp = requests.get(src,headers=headers)
        img_name = src.split('/')[-1] #url / 最后的内容
        
        with open('C:\\Users\\Oringals\\Desktop\\python\\crawler\\class2\\img' + str(img_name),'wb') as f:
            f.write(img_resp.content)
        if(last_img_name == img_name):
            pass
        else:
            total += 1
            print('[*] done!',img_name,total)
            last_img_name = img_name 
        #print('last_name:',last_img_name)
print('[*] over!!')
    



    
    

    


