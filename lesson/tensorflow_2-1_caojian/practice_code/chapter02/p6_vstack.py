import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.vstack((a, b))
# 打印结果将显示垂直堆叠后的数组
print(f"垂直堆叠后的数组为:\n {result}")  # 输出示例: 垂直堆叠后的数组为:
# [[1 2 3]
#  [4 5 6]]

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = np.vstack((a, b))
# 打印结果将显示垂直堆叠后的数组
print(f"垂直堆叠后的数组为:\n {result}")  # 输出示例: 垂直堆叠后的数组为:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
result = np.vstack((a, b))
# 打印结果将显示垂直堆叠后的数组
print(f"垂直堆叠后的数组为:\n {result}")  # 输出示例: 垂直堆叠后的数组为:
# [[1 2]
#  [3 4]
#  [5 6]]