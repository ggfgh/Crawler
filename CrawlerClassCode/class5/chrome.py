from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#创建一个浏览器对象
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--gpu")

browser = webdriver.Chrome(options=chrome_options)
browser.get('http://www.baidu.com')

print(browser.title)
