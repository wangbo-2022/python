from lxml import etree
import requests

url='https://xianning.zbj.com/search/service/?l=0&kw=saas&r=1'

response=requests.get(url)

html=response.content.decode()

with open('a.html','w',encoding='utf-8') as f:
    f.write(html)

tree=etree.HTML(html)

companyName=tree.xpath('//*/div[@class="shop-info text-overflow-line"]/text()')
price=tree.xpath('//*/div[@class="price"]/span/text()')
title=tree.xpath('//*/a[@class="serve-name text-overflow-line-two"]/text()')

print((companyName))
print((price))
print((title))