from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.keys import Keys

#无头设置
chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.add_argument("--proxy-server=http://113.238.142.208:3128")
chrome_options.add_argument("--disable-gpu")

web = Chrome(options=chrome_options)
web.get('https://www.vulbox.com/')

web.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/a').click()
time.sleep(1)
web.find_element_by_xpath('/html/body/div/div/div/div/header/div/ul/li[1]/div/span/a').click()
time.sleep(1)

# web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()

# 如何进入到新窗口
# selenium默认不切换窗口
web.switch_to.window(web.window_handles[-1])

#在新窗口中提取内容
job_detail = web.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/ul/li[1]/div/div/a/div[2]/div/h4/span').text
print(job_detail)

#关掉子窗口
web.close()

#变更selenium的窗口
web.switch_to.window(web.window_handles[0])
print(web.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div[1]/section[1]/div[4]/div[3]/div/div/div/div/div/div/table/tbody/tr[1]/td[3]/div/div/span[2]').text)
web.close()

# 获取iframe中的内容
# 拿到iframe,切换到iframe,获取数据
# iframe = web.find_element_by_xpath('iframe xpath')
# web.switch_to.frame(iframe)
# web.swith_to.default_content() #切换回原页面(测试)
# result = web.find_element_by_xpath('xpath').text
# print(result)