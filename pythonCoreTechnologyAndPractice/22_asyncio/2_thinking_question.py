import concurrent.futures
import multiprocessing
import time


# 思考题 求列表中元素的整数平方和 常规版本
def cpu_bound(number):
    print("number={}, result={}".format(number, sum(i * i for i in range(number))))


def calculate_sums(numbers):
    for number in numbers:
        cpu_bound(number)


def calcuter_normal(numbers):
    start_time = time.perf_counter()
    calculate_sums(numbers)
    end_time = time.perf_counter()
    print("普通版本，耗时{}秒".format(end_time - start_time))


# 思考题 并行版本
def calculate_sums_future(numbers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(cpu_bound, numbers)


def calcuter_future(numbers):
    start_time = time.perf_counter()
    calculate_sums_future(numbers)
    end_time = time.perf_counter()
    print("多进程版本，耗时{}秒".format(end_time - start_time))


# 思考题 动态规划版本
squ = {}  # 用来储存中间结果


def cpu_dp(number):
    result = 0
    for i in range(number):
        if i not in squ.keys():
            squ[i] = i * i
        result += squ[i]
    print("number={}, result={}".format(number, result))


def calculate_sums_dp(numbers):
    for number in numbers:
        cpu_dp(number)


def calcuter_dp(numbers):
    start_time = time.perf_counter()
    calculate_sums_dp(numbers)
    end_time = time.perf_counter()
    print("动态规划版本，耗时{}秒".format(end_time - start_time))


# 思考题的multiprocessing版本
def calculate_sums_multiprocessing(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


def calcuter_multiprocessing(numbers):
    start_time = time.perf_counter()
    calculate_sums_multiprocessing(numbers)
    end_time = time.perf_counter()
    print("multiprocessing版本，耗时{}秒".format(end_time - start_time))


if __name__ == "__main__":
    # 思考题
    numbers = [1000000 + x for x in range(10)]
    calcuter_normal(numbers)
    calcuter_future(numbers)
    calcuter_dp(numbers)
    calcuter_multiprocessing(numbers)
