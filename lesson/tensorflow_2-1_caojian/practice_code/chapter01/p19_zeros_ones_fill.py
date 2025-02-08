import tensorflow as tf

# 1. 全零张量
a = tf.zeros(shape=[2, 3])

# 2. 全一张量
b = tf.ones(4)

# 3. 填充张量
c = tf.fill([2, 2], 9)
print("a:", a)
print("b:", b)
print("c:", c)
