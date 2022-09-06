from selenium.webdriver import Edge
from selenium.webdriver.common.action_chains import ActionChains
import time

url="https://kyfw.12306.cn/otn/resources/login.html"

web=Edge()

web.get(url)

time.sleep(1)

web.find_element('xpath','//*[@id="J-userName"]').send_keys("18680384942")

time.sleep(1)

web.find_element('xpath','//*[@id="J-password"]').send_keys("tcyhwb060422")

time.sleep(1)

web.find_element('xpath','//*[@id="J-login"]').click()

time.sleep(1)

btn=web.find_element('xpath', '//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn,300,0).perform()

ActionChains(web).move_to_element_with_offset()



