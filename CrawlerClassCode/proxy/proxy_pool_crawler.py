import requests
import json
import pprint

url = 'http://10.10.10.136:5010/all'

def getallProxy()->list:
    r = requests.get(url)
    #pprint.pprint(r.json())
    return r.json()

if __name__ == '__main__':
    proxy_list = getallProxy()
    #print(proxy_list)
    for proxy in proxy_list:
        print(proxy['proxy'])
        with open('proxy_list.txt','a') as f:
            f.write(proxy['proxy']+'\n')
    
