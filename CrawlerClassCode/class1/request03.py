import requests

url = "https://movie.douban.com/j/chart/top_list"

#重新封装参数
params = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20",
}

headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

resp = requests.get(url=url,params=params,headers=headers)

print(resp.json())

resp.close()