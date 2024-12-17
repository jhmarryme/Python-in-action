import functools  # 应用举例 给函数加上计时功能
import time


def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print("函数{}运行耗时{}秒".format(func.__name__, (end - start) * 1000))
        return res

    return wrapper


@log_execution_time
def add(n):
    s = 0
    for i in range(n):
        s += i
    return s


res = add(10000)
print(res)


@log_execution_time
def multiply(n):
    s = 1
    for i in range(n):
        s = s * (i + 1)
    return s


res = multiply(100)
print(res)
