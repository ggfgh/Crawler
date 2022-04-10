import requests

url = 'https://fanyi.baidu.com/sug'
proxies = { "http": None, "https": None}

p = 'n'
while(p=='n' or p == ''):
    s = input("[*] 请输入你要翻译的英文单词:")
    dat = {
    "kw": s
    }


    #发送post请求,发送的数据必须放在字典中,通过data参数进行传递
    resp = requests.post(url,data=dat,proxies=proxies)
    print(resp.json()) #json =>dict
    with open("result.txt",'a') as f:
        f.write(str(resp.json()))
    p = input("[*] 是否退出程序:(y/n)")


#暂停
input()

resp.close()