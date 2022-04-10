import requests

url = 'http://10.10.10.139/post.php'

getPara = {
    "wd": "林俊杰"
    }

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47"
}

res = requests.get(url = url,params=getPara,headers=headers)
print(res.text)
print(res.url)
input()