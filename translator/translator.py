# -*- coding: utf-8 -*-
# @Time : 2022-4-11
# @Author : YaoW
# @Email: comedyyou@163.com
# @File: translator.py
# @Software: VS Code

import requests
import sys

def parse(url,keyword):
    """
    url:
        爬取的目标地址
    keyword:
        需要翻译的文字
    """
    data = {"kw": keyword}
    
    response = requests.post(url=url,data=data,timeout=5)

    json_data = response.json()['data']
    
    if(json_data==''):
        print("Not found this word!")
    else:
        print(json_data)
    
    with open("translator_log.txt",'a') as f:
        f.write(str(json_data))
    
    response.close()

def banner():
    banner = """Usage: python translator.py <keyword>"""
    print(banner)

def main():
    url = 'https://fanyi.baidu.com/sug'

    if(len(sys.argv)<=1):
        banner()
    else:
        keyword = sys.argv[1]
        parse(url, keyword)

if __name__ =='__main__':
    main()
