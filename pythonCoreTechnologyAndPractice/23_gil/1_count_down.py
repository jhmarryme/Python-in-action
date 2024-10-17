import time
from threading import Thread


# 单线程版
def CountDown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    n = 100000000
    start_time = time.perf_counter()
    CountDown(n)
    end_time = time.perf_counter()
    print("n = {}，单线程版耗时{}".format(n, end_time - start_time))
    # 多线程版
    start_time = time.perf_counter()
    t1 = Thread(target=CountDown, args=[n // 2])
    t2 = Thread(target=CountDown, args=[n // 2])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.perf_counter()
    print("n = {}，多线程版耗时{}".format(n, end_time - start_time))
