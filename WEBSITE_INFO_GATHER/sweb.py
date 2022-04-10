import socket
import os
import whois
import requests
import sys
import requests
from concurrent.futures import ThreadPoolExecutor

url_list = []
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"}

def usage():
    print('usage: python searchweb.py [模式] [域名]')
    print('[模式] -h --help')
    print('       -a --all')
    print('       -i --ip')
    print('       -c --cdn')
    print('       --child')
    print('       -w --whois')
#域名反查ip
def searchIp(url):
    ip = socket.gethostbyname(url)
    print('ip:',ip)

#识别目标是否存在CDN
#nslookup
def checkCdn(url):
    url = url.replace('http://','')
    url = url.replace('https://','')
    
    cdn_data = os.popen(f'nslookup {url}')
    cdn_datas = cdn_data.read()
    x = cdn_datas.count('.')
    if x > 10:
        print("cdn存在")
    else:
        print("cdn不存在")

#端口扫描
# ports = ['21','22','23','443','445','3389']
# server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# for port in ports:
#     result = server.connect_ex((ip,int(port)))
#     if result == 0:
#         print('port %s open' %port) 
#     else:
#         print('port %s close' %port)

# whois查询
def whois_check(url):
    data = whois.whois(url)
    print(data)

# 保存数据
def saveFile(url):
        with open('child.txt','a') as f:
            f.write(url+'\n')

# 子域名查询
def checkZym(url):    
    try:
        # 200 301 302 
        ip = socket.gethostbyname(url)
        print(url+' -> '+ip)
        saveFile(url)

    except Exception as e:
        #print("Error:",e)
        pass
        

def readurlDic(domain):
    domain = domain.replace('http://','')
    domain = domain.replace('https://','')
    domain = domain.replace('www.','')
    
    for zym_data in open('dic.txt','r'):
        zym_data = zym_data.replace('\n', '')
        child_url = zym_data + '.' + domain
        url_list.append(child_url)

def main():
    check = sys.argv[1]
    if check == '-h' or check == '--help':
        usage()
    
    url = sys.argv[2]
    #print(sys.argv)
    readurlDic(url)
    if check == '-a' or check == '--all':
        searchIp(url)
        checkCdn(url)
        whois_check(url)
        for url in url_list:
            checkZym(url)
        #print(url_list)
        #checkZym(url)
    
    if check == '-w' or check == '--whois':
        whois_check(url)
    
    if check == '-i' or check == '--ip':
        searchIp(url)
    
    if check == '-c' or check == '--cdn':
        checkCdn(url)  
    
    if check == '--child':
        with ThreadPoolExecutor(10) as t:
            for url in url_list:
                #print(url)
                t.submit(checkZym,url)
    
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        usage()
        print(f'Error:({e}'+')')



