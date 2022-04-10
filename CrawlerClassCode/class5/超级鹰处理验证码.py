from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
import chaojiying

opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
web = Chrome(options=opt)

web.get('https://uim.infinitus.com.cn/login?service=https://edealer.infinitus.com.cn/login/cas&appId=edealer-front&nextstep=https://gbss.infinitus.com.cn/front/gbss-portal-web/dealer/nextstep/1&forward=https://edealer.infinitus.com.cn/front?isFromWWW=1')
# web.find_element_by_xpath('//*[@id="login-btn"]').click()

#输入账号
web.find_element_by_xpath('//*[@id="userName"]').send_keys('15113205893')
sleep(2)

#输入密码
web.find_element_by_xpath('//*[@id="password"]').send_keys('123123')
sleep(2)

# 点击协议
web.find_element_by_xpath('//*[@id="agreeToAgreement"]').click()

# 识别验证码
img = web.find_element_by_xpath('//*[@id="loginCode"]').screenshot_as_png
chaojiying = chaojiying.Chaojiying_Client('comedy', '123.com', '924865')
dic = chaojiying.PostPic(img,1902)
verify_code = dic['pic_str']
print(verify_code)
sleep(2)

# 输入验证码
web.find_element_by_xpath('//*[@id="captchaResponse"]').send_keys(verify_code)
sleep(2)

#点击登录
web.find_element_by_xpath('//*[@id="loginBtn"]').click()
sleep(10)

#//*[@id="groupbox_pad_"]/div[2]/div[1]/div
#//*[@id="EDEALER_MY_CUSTOMER_WALLET"]
web.find_element_by_xpath('//*[@id="EDEALER_MY_CUSTOMER_WALLET"]').click()
text = web.find_element_by_xpath('//*[@id="groupbox_pad_"]/div[2]/div[1]/div').text
print(text)
sleep(2)

web.close()