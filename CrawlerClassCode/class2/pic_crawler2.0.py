import requests
import re
from bs4 import BeautifulSoup

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}


#下载图片的数量
total = 0
start = int(input('开始爬取的页面:'))
end = int(input('终止爬取的页面:'))
last_img_name = ''

for i in range(start,end+1):
    url = 'http://bbs.fengniao.com/forum/forum_101_{0}_lastpost.html'.format(i)
    hrefs = ''

    print('当前爬取主页:',url)
    resp = requests.get(url,headers=headers)
    main_page = BeautifulSoup(resp.text,"html.parser")
    #print(main_page)
    alist = main_page.find_all("a")
    #print(alist)

    for a in alist:
        href = a.get('href')
        #print(href)
        hrefs += str(href)
    #print(hrefs)

    #正则匹配图片子页面
    obj1 = re.compile(r"/forum/(?P<src>\d{8}).html",re.S)
    obj2 = re.compile(r'<img src="(?P<img_url>.*?).jpg')
    #obj3 = re.compile(r'<img src="(?P<img_url>.*?).png')
    
    #子页面
    result = obj1.finditer(hrefs)
    #请求获得的所有子页面
    for href in result:
        #图片所在的页面
        child_href = 'http://bbs.fengniao.com/forum/' + href.group('src') + '.html'
        #print(href)
        child_resp = requests.get(child_href,headers=headers)
        child_result = obj2.findall(child_resp.text)
        for img_href in child_result:
            
            #图片的url
            img_src = img_href + '.jpg'
            
            img_resp = requests.get(img_src,headers=headers)
            img_name = img_src.split('/')[-1]
            with open(str(img_name),"wb") as f:
                f.write(img_resp.content)
            if(last_img_name == img_name):
                pass
            else:
                total += 1
                print('[*] 成功下载%d张图片,当前下载图片页面%s,文件名%s' %(total,child_href,img_name))

print('[*] over')
   
        



