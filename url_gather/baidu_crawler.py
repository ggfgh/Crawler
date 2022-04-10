import requests
import re
import threading
import time
from bs4 import BeautifulSoup as bs
from queue import Queue
from argparse import ArgumentParser

arg = ArgumentParser(description='baidu_url_collection')
arg.add_argument('keyword',help='inurl:.asp?id=1')
arg.add_argument('-p', '--page', help='page count', dest='pagecount', type=int)
arg.add_argument('-t', '--thread', help='the thread_count', dest='thread_count', type=int, default=10)
arg.add_argument('-o', '--outfile', help='the file save result', dest='outfile', default='result.txt')
result = arg.parse_args()

headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)'}

class Bd_url(threading.Thread):
    def __init__(self, que):
        threading.Thread.__init__(self)
        self._que = que

    def run(self):
        while not self._que.empty():
            URL = self._que.get()
            try:
                self.bd_url_collect(URL)
            except Exception as e:
                print ('Exception: ',e)
                pass

    def bd_url_collect(self, url):

            r = requests.get(url, headers=headers, timeout=5)

            soup = bs(r.content, 'lxml', from_encoding='utf-8')
            bqs = soup.find_all(name='a', attrs={'data-click':re.compile(r'.'), 'class':None})
            for bq in bqs:

                r = requests.get(bq['href'], headers=headers, timeout=5)
                if r.status_code == 200:
                    print(r.url)

                    with open(result.outfile, 'a') as f:
                        f.write(r.url + '\n')

def main():
    thread = []
    thread_count = result.thread_count
    que = Queue()
    for i in range(0,(result.pagecount)):
        que.put('https://www.baidu.com/s?wd=' + result.keyword + '&pn=' + str(i))

    for i in range(thread_count):
        thread.append(Bd_url(que))

    for i in thread:
        i.start()

    for i in thread:
        i.join()

if __name__ == '__main__':

    start = time.perf_counter()
    main()
    end = time.perf_counter()

    urlcount = len(open(result.outfile,'r').readlines())

    with open(result.outfile, 'a') as f:
        f.write('--------use time:' + str(end-start) + '-----total url: ' + str(urlcount) + '----------------')


    print("total url: " + str(urlcount))
    print(str(end - start) + "s")
    
    f.close()
