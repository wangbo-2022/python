import requests
import os
import aiohttp
import asyncio
import aiofiles


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

    print("m3u8.txt下载完毕")

async def down_ts(name,url,session):

    async with session.get(url) as response:

        async with aiofiles.open(f"vedio/{name}ts.ts", "wb") as f:

            await f.write(await response.content.read())

    print(f"{name}ts.ts 下载完毕")


async def downTs(url):

    tasks=[]

    async with aiohttp.ClientSession() as session:

        async with aiofiles.open("m3u8.txt", "r",encoding="utf-8") as f:

            index = 0

            async for line in f:
                if line.startswith("#"):
                    continue

                line = line.strip()

                ts_url = url.split("/get")[0] + line

                if index < 10:
                    name = f"000{index}"
                elif index < 100:
                    name = f"00{index}"
                elif index < 1000:
                    name = f"0{index}"
                else:
                    name = f"{index}"

                index += 1

                task=asyncio.create_task(down_ts(name,ts_url,session))

                tasks.append(task)

            await asyncio.wait(tasks)






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

    asyncio.run(downTs(m3u8_url))

    # mergeTs()
