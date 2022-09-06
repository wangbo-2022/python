import asyncio
import time

async def func1():
    print(1)
    # time.sleep(2)
    await asyncio.sleep(2)
    print(2)


async def func2():
    print(3)
    # time.sleep(3)
    await asyncio.sleep(3)
    print(4)


async def func3():
    print(5)
    # time.sleep(4)
    await asyncio.sleep(4)
    print(6)


async def main():

    tasks=[
            asyncio.create_task(func1()),
            asyncio.create_task(func2()),
            asyncio.create_task(func3())
        ]
    await asyncio.wait(tasks)

if __name__=="__main__":

    t1=time.time()
    asyncio.run(main())
    t2=time.time()
    print(t2-t1)










