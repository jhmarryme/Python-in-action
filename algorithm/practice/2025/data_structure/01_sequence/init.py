"""
练习 1：基本操作热身
👉 写一个函数，初始化一个大小为 10 的数组，内容为 0-9，然后完成以下操作：
删除索引为 3 的元素
在索引 5 插入一个新元素 99
输出结果数组
🔎 提示：
删除用 pop() 或 del
插入用 insert(index, value)
注意索引是否从 0 开始？
"""
def_list = [i for i in range(10)]
print(def_list)
def_list.pop(3)
print(def_list)
def_list.insert(5, 99)
print(def_list)
