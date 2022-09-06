import requests
import os
from concurrent.futures import ThreadPoolExecutor

url = "https://chaoren.sc2yun.com/superman.php"


def get_m3u8_url(url):
    data = {
        "v": "fdc3074f5464e601",
        "type": "ml"
    }
    response = requests.post(url, data=data)

    return response.json()["url"]


def downLoadM3u8(url):

    response = requests.get(url)

    with open("m3u8.txt", "w", encoding="utf-8") as f:

        f.write(response.text)


def getTs(name, url):
    response = requests.get(url)

    with open(f"vedio/{name}ts.ts", "wb") as f:
        f.write(response.content)

    print(f"vedio/{name}ts.ts 下载完毕")


def downTs(url):

    with open("m3u8.txt", "r") as f:

        ts_url_list = []
        for line in f:
            if line.startswith("#"):
                continue

            line = line.strip()

            ts_url_list.append(url.split("/get")[0] + line)

    with ThreadPoolExecutor(50) as t:
        index = 0
        for ts_url in ts_url_list:

            if index < 10:
                name = f"000{index}"
            elif index < 100:
                name = f"00{index}"
            elif index < 1000:
                name = f"0{index}"
            else:
                name = f"{index}"

            t.submit(getTs, name, ts_url)

            index += 1


def mergeTs():
    lst = []

    with open("m3u8.txt", "r") as f:

        for line in f:
            if line.startswith("#"):
                continue

            line = line.strip()
            name = line[-15::]
            lst.append(f"vedio/{name}")

    s = "+".join(lst)

    # print(f"copy /b {s} movie.mp4")

    os.system(f"copy /b 5SYAE1DDRaNg.ts+pXZQQwDjYBbQ.ts vedio/movie.mp4")


if __name__ == '__main__':

    m3u8_url = get_m3u8_url(url)

    downLoadM3u8(m3u8_url)

    downTs(m3u8_url)

    # mergeTs()
