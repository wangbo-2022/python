from concurrent.futures import ThreadPoolExecutor
import requests
import csv

f=open("data.csv","w",encoding="utf-8")

csvWriter=csv.writer(f)

headers={
    "Referer": "http://www.xinfadi.com.cn/priceDetail.html",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
}

url="http://www.xinfadi.com.cn/getPriceData.html"

def func(data):

    response=requests.post(url=url,headers=headers,data=data)

    json_list=response.json()["list"]

    xinfadi=[]

    for item in json_list:
        xinfadi.append(item["prodName"])
        xinfadi.append(item["avgPrice"])

    csvWriter.writerow(xinfadi)

if __name__=="__main__":

    with ThreadPoolExecutor(50) as t:
        for i in range(200):
            data={
                "limit": 20,
                "current": i+1
            }
            t.submit(func,data)