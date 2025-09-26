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
        node = Node(val)
        if self.head is None:
            self.head = node
            return

        if self.tail is None:
            self.head.next_node = node
            self.tail = node
            return
        # todo
        pre = self.tail
        cur = self.head
        while cur.next_node is not None:
            cur = cur.next_node
        cur.next_node = node

    def insert(self, index, val):
        node = Node(val)
        if index == 0 and self.head is None:
            self.head = node
            return
        elif index == 0:
            head = self.head
            self.head = node
            node.next_node = head
            return
        pre = self.traverse_node(index - 1)
        if pre.next_node is None:
            pre.next_node = node
        else:
            tmp = pre.next_node
            node.next_node = tmp
            pre.next_node = node

    def delete(self, index):
        if index == 0 and self.head is None:
            return
        elif index == 0 and self.head is not None:
            self.head = self.head.next_node
            return

        pre = self.traverse_node(index - 1)
        if pre is None or pre.next_node is None:
            print(f'error, cannot find node {index}')
        pre.next_node = pre.next_node.next_node

    def traverse(self):
        if self.head is None:
            return
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next_node

    def traverse_node(self, index):
        count = 0
        cur = self.head
        while count < index and cur is not None:
            count += 1
            cur = cur.next_node
        return cur


linkedList = LinkedList()
linkedList.append("1")
linkedList.append("2")
linkedList.append("4")
linkedList.append("6")
linkedList.append("8")
linkedList.traverse()
print('---------')
linkedList.insert(2, "3")
linkedList.insert(4, "5")
linkedList.insert(6, "7")
linkedList.insert(0, "0")
linkedList.delete(0)
linkedList.traverse()
