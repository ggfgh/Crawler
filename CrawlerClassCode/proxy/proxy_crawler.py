import requests

def get_real_ip():
    url = 'http://httpbin.org/ip'
    proxy = {'http':'222.74.202.229:8080'}
    r = requests.get(url,proxies=proxy)
    print(r.text)

if __name__ == '__main__':
    get_real_ip()

