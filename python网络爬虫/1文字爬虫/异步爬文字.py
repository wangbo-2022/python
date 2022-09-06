# import asyncio
# import aiohttp
import requests


# url="https://boxnovel.baidu.com/boxnovel/wiseapi/chapterList?bookid=4306063500&pageNum=1&order=asc&site="

url="https://novel-content.cdn.bcebos.com/6742163417012457612"




response=requests.get(url)
response.encode="utf-8"
text=response.text

print(text)

# with open("a.txt","wb") as f:
#     f.write(response.content)


