import functools
import os
import time

import psutil

'''
迭代器/生成器性能对比
'''


# 显示当前 python 程序占用的内存大小

def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print("{} memory used: {}MB".format(hint, memory))


def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print("函数{}运行耗时{}秒".format(func.__name__, end - start))
        return res

    return wrapper


@log_execution_time
def test_iterator():
    show_memory_info("初始化迭代器")
    list1 = [i for i in range(10000000)]
    show_memory_info("初始化迭代器以后")
    print(sum(list1))
    show_memory_info("调用sum以后")


@log_execution_time
def test_generator():
    show_memory_info("初始化生成器")
    list2 = (i for i in range(10000000))
    show_memory_info("初始化生成器以后")
    print(sum(list2))
    show_memory_info("调用sum以后")


test_iterator()
print('----------------')
test_generator()
