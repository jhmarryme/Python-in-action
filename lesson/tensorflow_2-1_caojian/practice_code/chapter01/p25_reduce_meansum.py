import tensorflow as tf

# 1. 求平均值
# 示例1：全局平均值
tensor = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
global_mean = tf.reduce_mean(tensor)
print(f"全局平均值: {global_mean}")  # 结果：2.5

# 示例2：按行求平均值（axis=1）
row_mean = tf.reduce_mean(tensor, axis=1)
print(f"按行求平均值: {row_mean}")  # 结果：[1.5, 3.5]

# 示例3：按列求平均值（axis=0）
col_mean = tf.reduce_mean(tensor, axis=0)
print(f"按列求平均值: {col_mean}")  # 结果：[2, 3]

# 示例4：保持维度
keepdims_mean = tf.reduce_mean(tensor, axis=1, keepdims=True)
print(f"保持维度按行求平均值: {keepdims_mean}")  # 结果：[[1.5], [3.5]]

# 2. 求总和
# 示例1：全局总和
tensor = tf.constant([[1, 2], [3, 4]])
global_sum = tf.reduce_sum(tensor)
print(f"全局总和: {global_sum}")  # 结果：10

# 示例2：按行求和（axis=1）
row_sum = tf.reduce_sum(tensor, axis=1)
print(f"按行求和: {row_sum}")  # 结果：[3, 7]

# 示例3：按列求和（axis=0）
col_sum = tf.reduce_sum(tensor, axis=0)
print(f"按列求和: {col_sum}")  # 结果：[4, 6]

# 示例4：保持维度
keepdims_sum = tf.reduce_sum(tensor, axis=1, keepdims=True)
print(f"保持维度按行求和: {keepdims_sum}")  # 结果：[[3], [7]]
