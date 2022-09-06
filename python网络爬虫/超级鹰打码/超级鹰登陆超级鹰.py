from selenium.webdriver import Edge
from chaojiying import *
import time

url="https://www.chaojiying.com/user/login/"
# url = "https://www.lagou.com/"

web=Edge()

web.get(url)

time.sleep(1)

name="18680384942"
password="tcyhwb060422"

# 下载验证码图片
web.find_element('xpath','/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot("code.png")

# 读取验证码
chaojiying = Chaojiying_Client(name, password, '938674')

im = open('code.png', 'rb').read()

pic_str=chaojiying.PostPic(im, 1902)["pic_str"]

print(pic_str)

time.sleep(1)

# 输入用户名
web.find_element('xpath','/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys(name)

time.sleep(1)

# 输入密码
web.find_element('xpath','/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys(password)

time.sleep(1)

# 输入验证码
web.find_element('xpath','/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(pic_str)

time.sleep(1)

# 点击登陆
web.find_element('xpath','/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()

time.sleep(10)
