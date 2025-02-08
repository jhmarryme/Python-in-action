import tensorflow as tf

# 定义输入的类别索引
indices = tf.constant([1, 0, 3])
# 这里如果指定dtype=tf.float64会提示gpu相关错误
# indices = tf.constant([1, 0, 2], dtype=tf.float64)

# 定义类别总数
depth = 3
# 进行独热编码
one_hot_encoded = tf.one_hot(indices, depth)
print("简单示例的独热编码结果：")

print(one_hot_encoded.numpy())

indices = tf.constant([0, 1])
depth = 3
on_value = 2.0
off_value = -1.0

one_hot_encoded = tf.one_hot(indices, depth, on_value=on_value, off_value=off_value)
print("指定 on_value 和 off_value 的独热编码结果：")
print(one_hot_encoded.numpy())