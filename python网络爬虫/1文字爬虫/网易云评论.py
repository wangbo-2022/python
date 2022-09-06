import requests
import json

headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
}

url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

data={
    "params": "kT51VVT/zyR3zGvL13LXLnDe63lTj0arDC58go8ZJKoK8AKzTKyyC/NH76qeSF+V3Fi+tAcMUbQPuOdgBXA0SwBAU7q/U7oCClb3gVqIwjaT6ILUmzreot3vlaWh0wyuBL4XifhPD6auMTuU233/HK4gvtjDwRV88hh8avXEiFCQ5bdSPFcS+loLO/8NWgnK9fc+YwruszJi/xtcQfui8I9CHSY27Fe9RCb3GQtL6vo4Jf1RUXsjE2QqFAxOWfnnTBsKsb6uEnkCTB8bUDkKGyvWpoSe0oT1FI6TH+MZE34=",
    "encSecKey": "87f9365e46b55b4893daff1fd40eb963a685ad46541b23243988b3c1cab009bf2de176165e8a253e7eb6bfff2d86ca50bda0a4b0901831e89cd549d4131edcf367163233e55aa15f637f3bcc05187851ec23262315074d2bc14d0f9584e0f6e7a9fa06b371d6bb3417f05d33f34418e9260644715c77c942815c17c80ade77a3"
}

response=requests.post(url,data=data)

# jsonStr=str(response.json())

# with open('a.json','w',encoding='utf-8') as f:
#     f.write(jsonStr)

commentList=response.json()["data"]["hotComments"]

for item in commentList:
    print(item["content"])










