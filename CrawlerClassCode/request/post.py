import requests

postData = {
    "username":"admin",
    "passwd":"123.com"
}

url = 'http://10.10.10.139/post.php'

res = requests.post(url,data=postData)
print(res.text)
print(res.url)
input()