from email import header
import requests

# url='https://passport.17k.com/ck/user/login'

# data={
#     'loginName': '18680384942',
#     'password': 'tcyhwb060422'
# }

# session=requests.session()

# response=session.post(url,data=data)

# text=response.content.decode()

# print(response.cookies)

url='https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'

# response=session.get(url)

# print(response.content.decode())

headers={
    'Cookie':'GUID=a4e2ff85-628b-48ab-8704-3be1f51be67d; BAIDU_SSP_lcr=https://cn.bing.com/; Hm_lvt_9793f42b498361373512340937deb2a0=1662212534; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F18%252F98%252F05%252F98010598.jpg-88x88%253Fv%253D1662212755000%26id%3D98010598%26nickname%3D%25E4%25B9%25A6%25E5%258F%258B9M4G3B5lE%26e%3D1677765904%26s%3D6a92b9499f4b4d7b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2298010598%22%2C%22%24device_id%22%3A%2218303966feb47-07b6e59ac3161-72422e2e-921600-18303966fec3c3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24latest_referrer_host%22%3A%22cn.bing.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22a4e2ff85-628b-48ab-8704-3be1f51be67d%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1662214004'
}

response=requests.get(url,headers=headers)
print(response.content.decode())







