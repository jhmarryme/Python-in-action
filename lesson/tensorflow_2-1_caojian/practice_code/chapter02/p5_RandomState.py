import numpy as np

random_state = np.random.RandomState()
random_array = random_state.rand(5)
# 打印结果将显示生成的一维随机数组
print(
    f"生成的一维随机数组为: {random_array}")  # 输出示例: 生成的一维随机数组为: [0.84804975 0.59798924 0.88877848 0.06019478 0.11848782]

random_state = np.random.RandomState()
random_array = random_state.rand(2, 3)
# 打印结果将显示生成的二维随机数组
print(f"生成的二维随机数组为: {random_array}")  # 输出示例: 生成的二维随机数组为:
# [[0.60949388 0.95588547 0.08398618]
#  [0.12787878 0.89290513 0.78440364]]
