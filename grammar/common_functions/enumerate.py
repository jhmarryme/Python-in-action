'''
enumerate 是 Python 的一个内置函数，用于遍历序列（如列表、元组或字符串）时，同时获取元素的索引和值。它返回一个迭代器，该迭代器生成一个包含索引和值的元组。
    enumerate(iterable, start=0)
        iterable: 可迭代对象，如列表、元组、字符串等。
        start: 可选参数，用于设置索引的起始值，默认从 0 开始。
'''
# 1. 遍历列表时获取索引和值
fruits = ['apple', 'banana', 'cherry']

for index, value in enumerate(fruits):
    print(index, value)
'''
输出
0 apple
1 banana
2 cherry
'''

# 2. 自定义起始索引
fruits = ['apple', 'banana', 'cherry']
for index, value in enumerate(fruits, start=1):
    print(index, value)
'''
输出
1 apple
2 banana
3 cherry
'''

# 3. 使用 enumerate 构建字典
fruits = ['apple', 'banana', 'cherry']
fruit_dict = dict(enumerate(fruits))
print(fruit_dict)
'''
输出
{0: 'apple', 1: 'banana', 2: 'cherry'}
'''
