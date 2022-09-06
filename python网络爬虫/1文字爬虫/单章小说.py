import requests
import parsel


url='https://www.bbiquge.net/book/132488/53726615.html'

response=requests.get(url)
response.encoding='gbk'

selector = parsel.Selector(response.text)
title=selector.css('#main > h1::text').get()
title1=selector.xpath('//*[@id="main"]/h1/text()').get()
# print(title)
# print(title1)

content_list=selector.css('#content::text').getall()
content=''.join(content_list)
# print(content)

with open(f'C:\\Users\\wangbo\\Desktop\\study\\python\\python网络爬虫\\1文字爬虫\\深空彼岸\\{title}.txt',mode='w',encoding='utf-8') as f:
    f.write(title)
    f.write('\n')
    f.write(content)