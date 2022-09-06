import selenium
import requests
import os
import parsel
from selenium import webdriver
import time

def drop_down():

    for x in range(1,100,4):

        time.sleep(1)

        j=x/9

        js='document.documentElement.scrollTop=document.documentElement.scrollHeight * %f' % j

        driver.execute_script(js)



# filename='4视频爬虫/vedio/抖音/'

# if not os.path.exists(filename):
#     os.mkdir(filename)

url='https://www.douyin.com/user/MS4wLjABAAAA2io-5JaeJwYEv2WBOkhbK3xxYsXpOaPgPKr7pp3ZomM'

headers={
    'cookie': 's_v_web_id=verify_l5exeyke_hqzw7oVK_iLd5_4R8U_9XCm_HsDb0QZ2Tzow; passport_csrf_token=ef638bff9a0fbdbd5d1bcc24d235fd93; passport_csrf_token_default=ef638bff9a0fbdbd5d1bcc24d235fd93; ttwid=1%7CL02chpWse7QH9L4oRL0cHTGxwlMi18XABVHv1FiSGRg%7C1657434167%7Cda617099d215b1b97a835f37dfb105bf198df2140c65fcf2461c39833602b969; THEME_STAY_TIME=%22299580%22; IS_HIDE_THEME_CHANGE=%221%22; download_guide=%223%2F20220830%22; SEARCH_RESULT_LIST_TYPE=%22single%22; n_mh=ST8kziTGio8dce9HpXi6EJNTiYMWRBbwVZHH6vumCgQ; sso_uid_tt=9090137a19a06c3cde4f40bc274c29f3; sso_uid_tt_ss=9090137a19a06c3cde4f40bc274c29f3; toutiao_sso_user=0c4bfc0ebf73e4c664d624a65b2d0fa0; toutiao_sso_user_ss=0c4bfc0ebf73e4c664d624a65b2d0fa0; passport_auth_status=c0e1bda1b612eda148763a653010adbd%2C; passport_auth_status_ss=c0e1bda1b612eda148763a653010adbd%2C; sid_guard=950c32be4d36af0d7edb5bcd07c6a9fd%7C1661851335%7C5183998%7CSat%2C+29-Oct-2022+09%3A22%3A13+GMT; uid_tt=1eca02b08013ed08b23f0a6b5fef8aac; uid_tt_ss=1eca02b08013ed08b23f0a6b5fef8aac; sid_tt=950c32be4d36af0d7edb5bcd07c6a9fd; sessionid=950c32be4d36af0d7edb5bcd07c6a9fd; sessionid_ss=950c32be4d36af0d7edb5bcd07c6a9fd; sid_ucp_v1=1.0.0-KDJmZjE4MzFmZWJmNTY3OTJlNjYxNjNlOTQzZDhmY2E4MjBiMjJlMTYKFwjMgpuwjgIQx623mAYY7zEgDDgGQPQHGgJscSIgOTUwYzMyYmU0ZDM2YWYwZDdlZGI1YmNkMDdjNmE5ZmQ; ssid_ucp_v1=1.0.0-KDJmZjE4MzFmZWJmNTY3OTJlNjYxNjNlOTQzZDhmY2E4MjBiMjJlMTYKFwjMgpuwjgIQx623mAYY7zEgDDgGQPQHGgJscSIgOTUwYzMyYmU0ZDM2YWYwZDdlZGI1YmNkMDdjNmE5ZmQ; odin_tt=6cb0ca7116054daa5f1475147e1cc5466377da6cf9b7a357eb971b380b93f730b90df3be610893c7495ad5143a972cc9; sid_ucp_sso_v1=1.0.0-KDVkYmNjNjY1Y2IyNTViYjkyYThhNGZjMTA1ZDEyZWI1NmE3NTE5OWMKHQjMgpuwjgIQx623mAYY7zEgDDCVuJvPBTgGQPQHGgJsZiIgMGM0YmZjMGViZjczZTRjNjY0ZDYyNGE2NWIyZDBmYTA; ssid_ucp_sso_v1=1.0.0-KDVkYmNjNjY1Y2IyNTViYjkyYThhNGZjMTA1ZDEyZWI1NmE3NTE5OWMKHQjMgpuwjgIQx623mAYY7zEgDDCVuJvPBTgGQPQHGgJsZiIgMGM0YmZjMGViZjczZTRjNjY0ZDYyNGE2NWIyZDBmYTA; __ac_nonce=0630f6c5900a686c26fae; __ac_signature=_02B4Z6wo00f01r.yRWAAAIDCP.C.IGSgmLa.0kHAAM0ACtpq9wM1Zb-k8zVtQDRKPPsmXHBBUlQALKBNjjkJ1jxes7hhh0Fr2LkKs6fz4KUj9KYlARKuCeyDKZ63ADJzrRI9sFM7aXAfdmrC4c; douyin.com; strategyABtestKey=1661955162.025; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA5XMAXRvEVAhVfDEKFkuCkrbnYneVxYReyu1RBeOufl4%2F1661961600000%2F0%2F1661955162360%2F0%22; msToken=M8XcysX3b5NmBpttQW2egMrBqkXmlB7DwU1MNCBlSAt-DHGGALzVB1fs60EZF8YcYYX4H4sg0y0u7rIbJVqTmWq1Au3mAtuYUHyZlLcXZWx3-1ndBrUXQ8s=; home_can_add_dy_2_desktop=%221%22; tt_scid=k0N5kfqfAtQDYi9OxMPgYmvwNAPwhW9tooEDR-6tx7nSpf5K6fJ-1j7TSfIXY8dp823e; msToken=CTFd4_BEYYRYs-JIHJZnBk4OEXRVnsw-1nRWZy7q6t2f5n_5BuCGbCNgMWn_3nT0d__sp3csHGhEso_Qiv4a1DQxAqTzn9NDJt6Kkw4j47nKfURbFqCtjhQ=',
    'refere': 'https://www.douyin.com/user/MS4wLjABAAAA2io-5JaeJwYEv2WBOkhbK3xxYsXpOaPgPKr7pp3ZomM',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
    }

driver=webdriver.Edge()

driver.get(url)

time.sleep(3)

drop_down()

# response=requests.get(url=url,headers=headers)

# selector=parsel.Selector(response.text)

# url_list=selector.css('.Eie04v01 a::attr(href)').getall()

# for url in url_list:
    # vedio_url='https://www.douyin.com'+url

# headers={
#     'Host': 'v26-web.douyinvod.com',
#     'refere': 'https://www.douyin.com/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
#     }
    
# vedio_url='https://www.douyin.com/video/7133043535934164260'

# response=requests.get(url=vedio_url,headers=headers)

# with open('aa.html',mode='w',encoding='utf-8') as f:
#     f.write(response.text)

    # with open('vedio.mp4',mode='wb',encoding='utf-8') as f:
    #     f.write(data)