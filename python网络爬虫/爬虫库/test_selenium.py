from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.edge.options import Options

import time

url = "https://www.lagou.com/"

# 建立浏览器对象
web = Edge()

# 打开一个网站
web.get(url)

# 等待网页内容加载
time.sleep(1)

# 找到 “全国” 所在的元素
el = web.find_element('xpath', '//*[@id="changeCityBox"]/p[1]/a')

# 执行点击操作
el.click()

# 等待网页内容加载
time.sleep(1)

# 方法一：找到输入框 输入python 回车搜索
web.find_element('xpath',
                 '//*[@id="search_input"]').send_keys('python',
                                                      Keys.ENTER)

# # 方法二：找到输入框 输入python 点击搜索按钮
# input_tag = web.find_element('xpath', '//*[@id="search_input"]')
# input_tag.send_keys("python")
# el = web.find_element('xpath', '//*[@id="search_button"]')
# el.click()

# 等待网页内容加载
time.sleep(1)

web.find_element(
    'xpath',
    '//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()

web.switch_to.window(web.window_handles[-1])

# 等待网页内容加载
time.sleep(1)

# 抓取数据
job_details = web.find_element(
    'xpath', '//*[@id="job_detail"]/dd[2]/div').text.split()
for item in job_details:
    print(item)

# 等待网页内容加载
time.sleep(1)

# 关闭子窗口
web.close()
# 切回主窗口
web.switch_to.window(web.window_handles[0])


# 等待网页内容加载
time.sleep(1)

# 抓取数据
div_list = web.find_elements('xpath', '//*[@id="jobList"]/div[1]/div')

for div in div_list:
    job = div.find_element('xpath', './div[1]/div[1]/div[1]/a').text
    price = div.find_element('xpath', './div[1]/div[1]/div[2]/span').text
    company = div.find_element('xpath', './div[1]/div[2]/div[1]/a').text
    print(company, job, price)

web.close()

# url = "https://mjw21.com/dp/NDY3MS0xLTA=.html"
#
# web = Edge()
#
# web.get(url)
#
# # 等待网页内容加载
# time.sleep(1)
#
# #
# iframe = web.find_element('xpath', '//*[@id="vodplay"]')
#
# # 切换到iframe
# web.switch_to.frame(iframe)
#
# print(web.find_element('xpath', '/html/head/title').text)
#
# # 等待网页内容加载
# time.sleep(1)
#
# # 切回默认窗口
# web.switch_to.default_content()
# text = web.find_element('xpath', '/html/body/section/div/div/div[2]/h4/a').text
# print(text)

# 准备好参数
# opt=Options()
# opt.add_argument("--headless")
# opt.add_argument("--disable-gpu")
#
# url="https://www.endata.com.cn/BoxOffice/BO/Year/index.html"
#
# # 建立浏览器对象
# web = Edge(options=opt)
#
# # 打开一个网站
# web.get(url)
#
# # 等待网页内容加载
# time.sleep(1)
#
# sel_el=web.find_element('xpath','//*[@id="OptionDate"]')
#
# sel=Select(sel_el)
#
# # 按照索引切换
# for i in range(len(sel.options)):
#     sel.select_by_index(i)
#     time.sleep(1)
#     table=web.find_element('xpath','//*[@id="TableList"]/table')
#     print(table.text)
#     print("===================================================")
#
#
# print("运行完毕")

# # 页面经过数据加载以及js执行之后的html源码(element中)
# print(web.page_source)

# web.close()























