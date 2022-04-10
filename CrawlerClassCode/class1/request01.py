import requests

query = input("输入一个你喜欢的明星:")

url = f'https://cn.bing.com/search?q={query}&form=QBLH&sp=-1&pq=&sc=0-0&qs=n&sk=&cvid=5302145820824897B9A226AA28423AF7'
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
}

resp = requests.get(url,headers=headers)

f = open("search01.html","w",encoding="utf-8")
f.write(resp.text)
f.close()
#print(resp)
#print(resp.text)

resp.close()