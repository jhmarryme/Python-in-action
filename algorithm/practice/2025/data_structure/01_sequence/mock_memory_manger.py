"""
练习 2：模拟连续内存管理
我们把列表看作一块连续的内存，用 None 表示空闲。
实现一个类 MemoryManager：
初始化时传入一个大小 n，生成一个 [None]*n 的数组。

实现方法：
allocate(size)：找到连续 size 个 None，把它们标记成一个字符串（例如 "P1" 表示进程 1 占用），返回起始索引。
free(start, size)：释放从 start 开始的 size 个位置（还原为 None）。
show()：打印当前的“内存”情况。
"""
from typing import Optional


class MemoryManager:
    def __init__(self, n: int):
        self.memory: list[Optional[str]] = [None for _ in range(n)]

    def allocate(self, size: int, pid: str) -> int:
        if size <= 0 or size > len(self.memory):
            return -1
        index, count = -1, 0
        for i in range(len(self.memory)):
            if self.memory[i] is None:
                count += 1
            else:
                count = 0
            if count == size:
                index = i - size + 1
                self.memory[index:i + 1] = [pid] * size
                break
        return index

    def free(self, start: int, size: int) -> None:
        if start < 0 or size > len(self.memory):
            return

        for i in range(start, min(len(self.memory), start + size)):
            self.memory[i] = None

    def show(self) -> None:
        print(self.memory)


manager = MemoryManager(10)
manager.show()
manager.allocate(4, 'P1')
manager.show()
manager.allocate(3, 'P2')
manager.show()
manager.free(0, 2)
manager.show()
manager.free(5, 2)
manager.show()
