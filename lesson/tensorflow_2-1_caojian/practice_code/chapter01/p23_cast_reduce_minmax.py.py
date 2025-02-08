import tensorflow as tf

# 1. 类型转换
# 示例1：整型转浮点型
a = tf.constant([1, 2, 3], dtype=tf.int32)
b = tf.cast(a, dtype=tf.float32)
print(f"整型转浮点型结果: {b}")  # 结果：[1.0, 2.0, 3.0]

# 示例2：布尔值转整型
mask = tf.constant([True, False, True])
num_mask = tf.cast(mask, dtype=tf.int32)
print(f"布尔值转整型结果: {num_mask}")  # 结果：[1, 0, 1]

tensor = tf.constant([[1, 2], [3, 4]])
# 2. 求最大值
# 全局最大值
global_max = tf.reduce_max(tensor)
print(f"全局最大值: {global_max}")  # 结果：4

# 按列求最大值（axis=0）
col_max = tf.reduce_max(tensor, axis=0)
print(f"按列求最大值: {col_max}")  # 结果：[3, 4]

# 保持维度
keepdims_max = tf.reduce_max(tensor, axis=1, keepdims=True)
print(f"保持维度按行求最大值: {keepdims_max}")  # 结果：[[2], [4]]

# 3. 求最小值
min_value = tf.reduce_min(tensor)
print(f"全局最小值: {min_value}")  # 结果：1
