from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time

chrome_option = Options()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')
web = Chrome(options=chrome_option)

web.get('https://graph.qq.com/oauth/show?which=Login&display=pc&response_type=code&client_id=101375548&redirect_uri=http%3A%2F%2Fi.fkw.com%2FbindQQAccountNew.jsp%3FmodeType%3Dpc&state=82&scope=get_user_info,get_info')
time.sleep(2)

# # 定位到下拉列表
# sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]')
# # 对元素进行包装，包装成下拉菜单
# sel = Select(sel_el)
# # 让浏览器调整选项
# for i in range(len(sel.options)): # i就是每一个下拉框的索引位置
#     sel.select_by_index(i)  # 按照索引进行切换
#     time.sleep(2)
#     table = web.find_element_by_xpath('//*[@id="TableList"]')
#     print(table.text) 
#     print("=================================")
# print('over')

# web.close()

# 获取浏览器处理后的代码

print(web.page_source)