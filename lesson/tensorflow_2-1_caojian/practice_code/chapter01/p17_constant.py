import tensorflow as tf

# tf.constant(张量内容, dtype=数据类型(可选))
a = tf.constant([1, 5], dtype=tf.int64)
print("a:", a)
print("a.dtype:", a.dtype)
print("a.shape:", a.shape)

# 本机默认 tf.int32  可去掉dtype试一下 查看默认值

# 创建标量
scalar = tf.constant(3.14, dtype=tf.float32)
# 创建向量
vector = tf.constant([1, 2, 3], dtype=tf.int32)
# 创建矩阵
matrix = tf.constant([[1.0, 2.0], [3.0, 4.0]])
print(scalar)
print(vector)
print(matrix)
