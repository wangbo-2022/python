import requests
import parsel
import os

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}

url='https://www.jdlingyu.com/tuji'

response=requests.get(url,headers=headers)

selector = parsel.Selector(response.text)

url_list=selector.css('.post-info > h2 > a::attr(href)').getall()
title_list=selector.css('.post-info > h2 > a::text').getall()

for item in zip(url_list,title_list):

    url=item[0]
    title=item[1]

    print(f'正在爬取{title}')

    filename=f'3图片爬虫/jdly/{title}'

    if not os.path.exists(filename):
        os.mkdir(filename)

    response=requests.get(url,headers=headers)

    selector=parsel.Selector(response.text)

    img_url_list=selector.css('.entry-content img::attr(src)').getall()


    for index in img_url_list:
        # print(index)
        img_data=requests.get(index,headers=headers).content

        img_name=index.split('/')[-1]

        with open(f'3图片爬虫/jdly/{title}/{img_name}',mode='wb') as f:
            f.write(img_data)

        print(f'{img_name}爬取成功')
    