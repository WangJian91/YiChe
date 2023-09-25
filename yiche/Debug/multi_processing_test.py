# -*- coding: utf-8 -*-
from multiprocessing import Process, Lock, Queue
import time
import os

# def task(name):
#     print("%s is runnig" % name)
#     time.sleep(3)
#     print("process is done")
#
#
# if __name__ == '__main__':
#     text_l = ("北京著名景点", "You are a Language Retelling Engineer.")
#     for i in range(5):
#         p = Process(target=task, kwargs={"name":"egon"})
#         p.start()
#         print("=======")

# class MyProcess(Process):
#     def __init__(self,name):
#         super(MyProcess,self).__init__()
#         self.name = name
#
#     def run(self):
#         print('%s is running' % self.name)
#         time.sleep(3)
#         print('%s is done' % self.name)
#
#
# if __name__ == '__main__':
#     p = MyProcess('egon')
#     p.start()
#     print('主')


# def task(name):
#     print("%s is runnig" % name)
#
#
# if __name__ == "__main__":
#     # p= Process(target=task,args=("egon",))
#     for i in range(10):
#         p = Process(target=task, args=(i,))
#         p.start()   # 向操作系统发送请
#         p.join()    # 让父进程等待子进程死亡
#         print("=======")


# def task(name):
#     print("%s is runnig"%name)
#
#
# if __name__ == "__main__":
#     # p= Process(target=task,args=("egon",))
#     p_list = []
#     for i in range(10):
#         p = Process(target=task, args=(i,))
#         p_list.append(p)
#         p.start()   # 向操作系统发送请求
#
#     for p in p_list:
#         p.join()    # 让父进程等待子进程死亡
#         print("=======")


# def task(name):
#     print("%s is runnig" % name)
#     time.sleep(1)
#     print("%s process is done" % name)
#
#
# if __name__ == "__main__":
#     p = Process(target=task, kwargs={"name": "egon"})
#     p.start()
#     print(p.pid)    # 进程p的id
#     print(p.name)   # 进程p的名字
#     p.terminate()    # 强制终止进程
#     p.join()
#     print(p.is_alive())     # 进程是否存在


# # 进程之间的物理隔离
# x = 1000
# def task(name):
#     global x
#     x = 0  # 修改的是子进程自己的属性x，因为内存的物理隔离，所以子进程的修改不会影响到父进程
#     print("%s is runnig" % name)
#     time.sleep(1)
#     print("process is done", x)  # 打印的是子进程的数据
#
#
# if __name__ == "__main__":
#     # p= Process(target=task,args=("egon",))
#     p = Process(target=task, kwargs={"name": "egon"})
#     p.start()
#     p.join()  # 让父进程等待子进程死亡
#     print("=======")
#     print(x)  # 打印的是父进程的属性


# # 并发运行,效率高,但竞争同一打印终端,带来了打印错乱
# def work():
#     print('%s is running' % os.getpid())
#     time.sleep(2)
#     print('%s is done' % os.getpid())
#
#
# if __name__ == '__main__':
#     for i in range(3):
#         p = Process(target=work)
#         p.start()


# # 由并发变成了串行,牺牲了运行效率,但避免了竞争
# def work(lock):
#     lock.acquire()
#     print('%s is running' % os.getpid())
#     time.sleep(2)
#     print('%s is done' % os.getpid())
#     lock.release()
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(3):
#         p = Process(target=work, args=(lock,))
#         p.start()
#         print('=========')


# q.put方法用以插入数据到队列中，put方法还有两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。如果超时，会抛出Queue.Full异常。如果blocked为False，但该Queue已满，会立即抛出Queue.Full异常。q.get方法可以从队列读取并且删除一个元素。同样，get方法有两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，那么在等待时间内没有取到任何元素，会抛出Queue.Empty异常。如果blocked为False，有两种情况存在，如果Queue有一个值可用，则立即返回该值，否则，如果队列为空，则立即抛出Queue.Empty异常.q.get_nowait():同q.get(False)q.put_nowait():同q.put(False)q.empty():调用此方法时q为空则返回True，该结果不可靠，比如在返回True的过程中，如果队列中又加入了项目。q.full()：调用此方法时q已满则返回True，该结果不可靠，比如在返回True的过程中，如果队列中的项目被取走。q.qsize():返回队列中目前项目的正确数量，结果也不可靠，理由同q.empty()和q.full()一样
'''multiprocessing模块支持进程间通信的两种主要形式:管道和队列都是基于消息传递实现的,但是队列接口'''

q = Queue(3)
# put ,get ,put_nowait,get_nowait,full,empty
q.put(1)
q.put(2)
q.put(3)
print(q.full())     # 满了
print(q.get())
print(q.get())
print(q.get())
print(q.empty())    # 空了
















