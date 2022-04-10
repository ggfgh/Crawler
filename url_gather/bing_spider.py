import requests,re,time
import threading
from argparse import ArgumentParser
from queue import Queue
from lxml import etree

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"}

arg = ArgumentParser(description='bing_url_collection')
arg.add_argument('keyword',help='inurl:.asp?id=1')
arg.add_argument('-p','--page',help='page count',dest='pagecount',type=int)
arg.add_argument('-t','--thread',help='the thread_count',dest='thread_count',type=int,default=10)
arg.add_argument('-o','--outfile',help='the file save result',dest='outfile',default='bing_url.txt')
result = arg.parse_args()

class By_url(threading.Thread):
    def __init__(self,que):
        threading.Thread.__init__(self) # 继承
        self._que = que 
    
    # run函数自动执行
    def run(self):
        while not self._que.empty():
            URL = self._que.get()
            try:
                self.by_url_collect(URL)
            except Exception as e:
                print('Exception:',e)
                continue
    # /h2/a
    def by_url_collect(self,url):
        resp = requests.get(url,headers=headers,timeout=5)
        soup = etree.HTML(resp.text)
        # <a target="_blank" href
        urls = soup.xpath('//h2/a[@target="_blank"]/@href')
        
        for url in urls:            
            #判断url是否可以访问
            try:
                r = requests.get(url,headers=headers,timeout=5)
                if r.status_code == 200:
                    print(r.url)
                    if '?' in r.url:
                        with open(result.outfile,'a') as f:
                            f.write(r.url + '\n')
                    else:
                        with open('all.txt','a') as f:
                            f.write(r.url+'\n')

            except Exception as e:
                print('Error:',e)

def main():
    thread = []
    thread_count = result.thread_count
    que = Queue()
    # https://cn.bing.com/search?q={query}&first={page_para}' #0 10 20 30
    for i in range(0,(result.pagecount * 10),10):
        que.put(f"https://cn.bing.com/search?q={result.keyword}&first={i}")
    
    for i in range(thread_count):
        thread.append(By_url(que))
    
    for i in thread:
        i.start()
    
    for i in thread:
        i.join()

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    urlcount = len(open(result.outfile,'r').readlines())
    with open(result.outfile,'a') as f:
        f.write('-' * 5 + 'use time:' + str(end-start) + '-' * 5 + 'total url: ' + str(urlcount) + '-' * 5 + '\n')
    
    print("[*] total url:" + str(urlcount))

    