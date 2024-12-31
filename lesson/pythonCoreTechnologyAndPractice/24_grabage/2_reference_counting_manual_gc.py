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


# 显示初始内存使用情况
show_memory_info('initial')

# 创建一个包含 1000 万个元素的列表
a = [i for i in range(10000000)]

# 显示创建列表后的内存使用情况
show_memory_info('after a created')

# 删除列表 a 的引用
del a

# 手动触发垃圾回收
gc.collect()

# 显示程序结束后的内存使用情况
show_memory_info('finish')

# 尝试访问已删除的变量 a（会抛出异常）
print(a)
