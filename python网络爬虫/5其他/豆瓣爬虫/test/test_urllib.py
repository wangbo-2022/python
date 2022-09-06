# -*- coding = utf-8 -*-

from bs4 import BeautifulSoup           # 页面解析 获取数据
import re                               # 正则表达式 进行文字匹配
import urllib.request                   # 指定URL 获取网页数据
import urllib.parse
import xlwt                             # 进行excel操作
import sqlite3                          # 进行SQLite数据库操作

# # 获取get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))

# # 获取post请求
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data)
# print(response.read().decode("utf-8"))

# # 超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")

# url = "http://httpbin.org/post"
# headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62"
# }
# data = bytes(urllib.parse.urlencode({"name": "python"}), encoding="utf-8")
#
# req = urllib.request.Request(url=url, data=data, headers=headers)
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

url = "https://movie.douban.com/top250"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62"
}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
