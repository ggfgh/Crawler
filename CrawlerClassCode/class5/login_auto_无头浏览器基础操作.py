from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

start = time.time()

chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
#chrome_options.add_argument('--headless')

web = webdriver.Chrome(options=chrome_options)
web.get('https://lagou.com')

#找到元素
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
el.click()  #点击事件   

#避免错误
time.sleep(1)

#找到输入框
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("渗透测试",Keys.ENTER)
time.sleep(1)

# 查找存放的数据
li_list = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')

for li in li_list:
    job_name = li.find_element_by_tag_name("h3").text
    job_money = li.find_element_by_xpath('./div[1]/div[1]/div[2]/div/span').text
    place = li.find_element_by_xpath('./div/div[2]/div/a').text
    with open(".\\lagou.txt",'a') as f:
        print(job_name,job_money,place)
        f.write(f"{job_name},{job_money},{place}\n")

end = time.time()
print('cost time %s s' %(end - start))