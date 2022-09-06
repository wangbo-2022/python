from wsgiref.headers import Headers
import requests

# headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
# }

# url='https://www.baidu.com'

# response=requests.get(url)

# print(len(response.text))
# with open('aa.html','w',encoding='utf-8') as f:
#     f.write(response.content.decode())

# response1=requests.get(url,headers=headers)

# print(len(response1.text))
# with open('ab.html','w',encoding='utf-8') as f:
#     f.write(response1.content.decode())


# url='https://www.baidu.com/s?wd=python'

# params={
#     'wd':'python'
# }

# response=requests.get(url,headers=headers)

# print(response)

# with open('aa.html','w',encoding='utf-8') as f:
#     f.write(response.content.decode())


headers={
    'cookie': '_octo=GH1.1.30005792.1658745274; _device_id=5d3edbb4a1d7c1e16a59c765be27401f; user_session=VBQ6_XsceppojHVtLVeJ8Az9DFac41D73NfvTRs_siqrb18b; __Host-user_session_same_site=VBQ6_XsceppojHVtLVeJ8Az9DFac41D73NfvTRs_siqrb18b; logged_in=yes; dotcom_user=wangbo-2022; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=Asia%2FShanghai; preferred_color_mode=light; has_recent_activity=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}

url='https://github.com/wangbo-2022'

response=requests.get(url,headers=headers)
with open('aa.html','w',encoding='utf-8') as f:
    f.write(response.content.decode())

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}

response1=requests.get(url,headers=headers)
with open('ab.html','w',encoding='utf-8') as f:
    f.write(response1.content.decode())











