import threading
import time


class simple_thread(threading.Thread):

    def __init__(self, name, delta_time):
        threading.Thread.__init__(self)
        self.delta_time = delta_time
        self.name = name

    def run(self):
        t = 0
        while t <= 10:
            print(f"In thread {self.name}, t={t}")
            time.sleep(self.delta_time)
            t += 1


thread1 = simple_thread("A", 1)
thread2 = simple_thread("B", 0.5)


# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("所有线程结束")

Threads = [thread1, thread2]


class monitor_thread(threading.Thread):

    def __init__(self, threads):
        threading.Thread.__init__(self)
        self.threads = {}
        for i in range(len(threads)):
            self.threads[i] = {}
            self.threads[i]["thread"] = threads[i]
            self.threads[i]["alive"] = True

    def run(self):
        while True:
            for t in self.threads:
                if self.threads[t]["alive"] and not self.threads[t]["thread"].is_alive():
                    self.threads[t]["alive"] = False
                    print("Thread %s is down." % self.threads[t]["thread"].getName())
            all_done = True
            for t in self.threads:
                if self.threads[t]["alive"]:
                    all_done = False
                    break
            if all_done:
                break
            time.sleep(0.9)


thread3 = monitor_thread(Threads)

for t in Threads:
    t.start()
thread3.start()
for t in Threads:
    t.join()
thread3.join()

# 队列操作
NumList = [i for i in range(10)]
n = 0


class square_thread(threading.Thread):

    def __init__(self, i):
        threading.Thread.__init__(self)
        self.i = i

    def run(self):
        global n
        global NumList
        while n <= 9:
            print(f"In thread {self.i}, number={NumList[n]}, result={NumList[n]**2}")
            n += 1
            time.sleep(1)


threads = []
# for i in range(3):
#     threads.append(square_thread(i))
#     threads[i].start()
# for i in range(3):
#     threads[i].join()


from queue import Queue

NumQueue = Queue()
for i in range(10):
    NumQueue.put(i)
while NumQueue.qsize() > 0:
    print(f"{NumQueue.get()} is get from NumQueue.")


# 生产者
class producer(threading.Thread):

    def __init__(self, begin_num):
        super().__init__()
        self.begin_num = begin_num

    def run(self):
        for i in range(5):
            NumQueue.put(self.begin_num + i)
            time.sleep(0.001)


# 消费者
class consumer(threading.Thread):
    def __init__(self, i):
        super().__init__()
        self.i = i

    def run(self):
        while NumQueue.qsize() > 0:
            num = NumQueue.get()
            print(f"In thread {self.i}, {num}^2={num**2}")
            time.sleep(1)


# # 两个生产者，一个从0开始，一个从10开始：
# Producer = []
# for i in range(2):
#     Producer.append(producer(10 * i))
#     Producer[i].start()
# # 三个消费者
# Customer = []
# for i in range(3):
#     Customer.append(consumer(i))
#     Customer[i].start()
# for i in range(3):
#     Customer[i].join()