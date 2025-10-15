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

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = list(map(list, zip(*matrix)))
print(f"转置后的矩阵: {transposed_matrix}")
transposed_matrix = [list(row) for row in zip(*matrix)]
print(f"转置后的矩阵: {transposed_matrix}")