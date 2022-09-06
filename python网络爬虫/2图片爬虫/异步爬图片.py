import asyncio
import aiohttp

urls=["http://pic.bizhi360.com/bpic/30/10630.jpg",
        "http://pic.bizhi360.com/bpic/57/10557.jpg",
        "http://pic.bizhi360.com/bpic/47/10547.jpg"
    ]


async def asyncDownLoad(url):

    name=url.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(name,"wb") as f:
                f.write(await response.content.read())


async def main():

    tasks=[]

    for url in urls:
        tasks.append(asyncio.create_task(asyncDownLoad(url)))
    
    await asyncio.wait(tasks)


if __name__=="__main__":

    asyncio.run(main())