import json
from urllib import request
from urllib import parse

headers={
    'Referer': 'http://www.kfc.com.cn/kfccda/storelist/index.aspx',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}

# post请求地址
post_url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
# post请求表单（参数）
data_dict={
    'cname': '',
    'pid': '',
    'keyword': '武汉',
    'pageIndex': '1',
    'pageSize': '10'
}
for index in range(1,6):

    data_dict['pageIndex']=index

    # post 请求首先做一次urlencode 
    data=parse.urlencode(data_dict)
    # post 参数必须时bytes
    data=data.encode('utf-8')
    # 封装post请求的对象
    rq=request.Request(url=post_url,headers=headers,data=data)

    response=request.urlopen(rq)

    text=response.read().decode('utf-8')

    json_obj=json.loads(text)

    for item in json_obj['Table1']:
        print(item['rownum'],item['storeName'],item['addressDetail'])

