import requests
import re
import os

filename='3图片爬虫\\img\\'

if not os.path.exists(filename):
    os.mkdir(filename)

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}

url='https://www.kanxiaojiejie.com/'

response=requests.get(url=url,headers=headers)

img_url=re.findall('<img fifu-featured="1" width="520" src="(.*?)"',response.text)

cnt=1

for item in img_url:
    response=requests.get(item)
    img_data=response.content

    with open(f'3图片爬虫\img\img{cnt}.png',mode='wb') as f:
        f.write(img_data)

    print(f'img{cnt}爬取完成')

    cnt +=1
