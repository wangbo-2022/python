from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from multiprocessing import Process
from unicodedata import name

# def func(name):

#     for i in range(10):
#         print(name,i)

# class myThread(Thread):
#     def run(self):
#         for i in range(10):
#             print("子线程",i)


# if __name__=="__main__":

#     t1=Thread(target=func,args=("子进程一",))
#     t1.start()

#     t2=Thread(target=func,args=("子进程二",))
#     t2.start()

#     # t1=myThread()

#     for j in range(10):
#         print("主线程",j)


def func(name):

    for i in range(1000):
        print(name,i)

if __name__=="__main__":

    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(func,name=f"线程{i}")

    print("线程执行完毕")

