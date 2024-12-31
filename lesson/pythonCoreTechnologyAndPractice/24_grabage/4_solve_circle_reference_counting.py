import gc
import os

import psutil


# 显示当前 Python 程序占用的内存大小
def show_memory_info(hint):
    # 获取当前进程 ID
    pid = os.getpid()
    # 获取当前进程对象
    p = psutil.Process(pid)

    # 获取进程的内存信息
    info = p.memory_full_info()
    # 计算内存使用量（单位：MB）
    memory = info.uss / 1024. / 1024
    # 打印内存使用信息
    print('{} memory used: {} MB'.format(hint, memory))


# 测试函数
def func():
    # 显示初始内存使用情况
    show_memory_info('initial')

    # 创建两个大列表
    a = [i for i in range(10000000)]  # 列表 a，包含 1000 万个元素
    b = [i for i in range(10000000)]  # 列表 b，包含 1000 万个元素

    # 显示创建列表后的内存使用情况
    show_memory_info('after a, b created')

    # 创建循环引用：a 引用 b，b 引用 a
    a.append(b)
    b.append(a)


# 调用测试函数
func()

# 手动触发垃圾回收
gc.collect()

# 显示程序结束后的内存使用情况
show_memory_info('finished')
