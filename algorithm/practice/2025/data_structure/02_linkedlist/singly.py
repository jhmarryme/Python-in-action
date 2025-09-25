"""
Step 1：单链表
👉 先实现一个 Node 类，再用它搭建一个 LinkedList 类。
节点 Node：包含 val 和 next
链表 LinkedList：包含
append(val) 在尾部追加
insert(index, val) 在指定位置插入
delete(index) 删除指定位置
traverse() 遍历输出所有节点

练习题 1：
用单链表存储 [1, 2, 3]
在索引 1 插入元素 99
删除索引 0 的元素
遍历输出最终链表
"""
from typing import Optional


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail = None
        pass

    def append(self, val):
        if (self.head is None):
            self.head = Node(val)
            return

        if (self.tail is None):
            self.tail = Node(val)
            self.head.next_node = self.tail
            return
        node = Node(val)
        pre_tail = self.tail
        pre_tail.next_node = node
        self.tail = node

    def insert(self, index, val):
        pass

    def delete(self, index):
        pass

    def traverse(self):
        if self.head is None:
            return
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next_node


linkedList = LinkedList()
linkedList.append("1")
linkedList.append("2")
linkedList.append("3")
linkedList.append("4")
linkedList.append("5")
linkedList.traverse()
