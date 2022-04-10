import requests

def login():

    login_url = 'https://passport.17k.com/ck/user/login'
    
    session = requests.session()
    
    data = {
        
        'loginName':'15113205893',
        'password':'123.com',
    }
    headers = {
        'Referer': 'https://passport.17k.com/login/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        #'Cookie': 'IPLOC=CN; SUV=0010F8CF75885A32617594C5FF5D6671'
    }

    r = session.post(login_url,data=data,headers=headers)
    r.encoding='utf-8'
    #print(r.text)
    return session

def getContent(session):
    
    url = 'https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'
    
    headers={
         #'Referer': 'https://user.17k.com/www/bookshelf/index.html',
         #'Cookie':'GUID=dd7b4b66-b631-481c-bd70-9ef289d41fc4; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2284234596%22%2C%22%24device_id%22%3A%2217cb36775769-0331a9fad34a298-4c3e2679-1382400-17cb3677577263%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22dd7b4b66-b631-481c-bd70-9ef289d41fc4%22%7D; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1635097475; Hm_lpvt_9793f42b498361373512340937deb2a0=1635098049; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F16%252F96%252F45%252F84234596.jpg-88x88%253Fv%253D1635097622000%26id%3D84234596%26nickname%3Dcomdyore%26e%3D1650650015%26s%3D0b95c540d2065ede'
    }
    
    resp = session.get(url)
    resp.encoding='utf-8'
    
    json_text = resp.json()
    #print(json_text)
    json_list = json_text['data']
    
    for book in json_list:
        print(book['bookName'])

if __name__ == '__main__':
    getContent(login())


