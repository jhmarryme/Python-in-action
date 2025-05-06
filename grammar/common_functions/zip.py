# 示例主要逻辑说明：使用 zip 函数从两个列表构建字典
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
person_dict = dict(zip(keys, values))
print(person_dict)

# 示例主要逻辑说明：对两个列表进行组合
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))
