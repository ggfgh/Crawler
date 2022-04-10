import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

#contID_list = []

def mian():
    i = 0
    url = 'https://www.pearvideo.com/category_8'
    headers = {
        'Referer':'https://www.baidu.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'
    }

    #<a href="video_1744464" class="actwapslide-link">
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    content = requests.get(url,headers=headers,verify=False).text
    soup = BeautifulSoup(content,"html.parser")
    a_list = soup.find_all('a',class_='vervideo-lilink actplay')

    for a in a_list:
        contID = a.get('href').split('_')[1]
        #contID_list.append(contID)
        print(f'========= 正在下载{i+1}个视频 =========')
        donwnloadVideo(contID)
        i += 1
        print(f'成功下载{i}个视频')

def donwnloadVideo(contID):
    jsonUrl = f'https://www.pearvideo.com/videoStatus.jsp?contId={contID}'
    headers = {
        'Referer':f'https://www.pearvideo.com/video_{contID}',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'
    }
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    r = requests.get(jsonUrl,headers=headers,verify=False)
    json_data = r.json()

    time = json_data['systemTime']
    videoSrc = json_data['videoInfo']['videos']['srcUrl']
    #print('time:',time,'videoSrc:',videoSrc)

    #"https://video.pearvideo.com/mp4/adshort/20211025/1635226203796-15787050_adpkg-ad_hd.mp4"
    #获取视频实际地址https://video.pearvideo.com/mp4/adshort/20211025/cont-1744464-15787050_adpkg-ad_hd.mp4""
    #网页地址https://www.pearvideo.com/video_1744464
    contentUrl = f'https://www.pearvideo.com/video_{contID}'
    videoHz = contentUrl.split('_')[1]
    videoSrc = videoSrc.replace(time,f"cont-{videoHz}")

    #下载视频
    video = requests.get(videoSrc,headers=headers,verify=False).content
    with open(f"{videoHz}.mp4",'wb') as f:
        print(f'{videoHz}.mp4')
        f.write(video)
        f.close()

if __name__ == '__main__':
    main()


