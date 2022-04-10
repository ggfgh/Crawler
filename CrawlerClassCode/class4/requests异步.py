import asyncio
import aiohttp
import aiofiles,time
import requests

urls = [
    "http://kr.shanghai-jiuxin.com/file/2021/1105/419e535e83c7192a99f7ee76d15f4043.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/1105/8b5586ee3febf914369de58aee65a370.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0222/da6aec6d7e061dd6ea5da7cbe90e4abc.jpg"
]

async def aiodownload(url):
    
    img_name = url.split('/')[-1] 
    #requests
    
    async with aiohttp.ClientSession() as session:
         
         async with session.get(url) as r:
            #  r.content.read() #r.text() r.json()
            
            #文件的异步操作aiofiles
            img = await r.content.read()
            
            async with aiofiles.open(".\\img\\"+str(img_name),mode='wb') as f:
                await f.write(img)
                # f.write(await r.content.read()) #读取内容是异步的

def normaldownload(url):
    
    img_name = url.split('/')[-1]
    r = requests.get(url)
    
    with open(img_name,'wb') as f:
        f.write(r.content)

async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
        #print(aiodownload(url))
    
    await asyncio.wait(tasks)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    # for url in urls:
    #     normaldownload(url)
    end = time.time()
    print("cost time %f" %(end - start))