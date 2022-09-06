import requests
import parsel
import re

url_book='https://www.bbiquge.net/book/132488/'

response = requests.get(url_book)

url_index=re.findall('<option value="/book/132488/(.*?)".*?>.*?</option>',response.text)

name='深空彼岸'

for item in url_index:
    url_page = url_book+item

    response=requests.get(url_page)
    href=re.findall('<dd><a href="(.*?)">.*?</a></dd>',response.text)

    for index in href:
        url_content=url_book+index
        response=requests.get(url_content)

        selector=parsel.Selector(response.text)

        title=selector.css('#main > h1::text').get()

        content_list=selector.css('#content::text').getall()
        content=''.join(content_list)

        with open(f'C:\\Users\\wangbo\\Desktop\\study\\python\\python网络爬虫\\1文字爬虫\\深空彼岸\\{name}.txt',mode='a',encoding='utf-8') as f:
            f.write(title)
            f.write('\n')
            f.write(content)
            f.write('\n')