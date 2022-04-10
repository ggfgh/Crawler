import requests

url = "https://www.baidu.com"

try:
    res = requests.get(url,timeout=3)
    print(res.text)

except Exception as e:
    print("timeout")