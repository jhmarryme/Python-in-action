import tensorflow as tf

# 正态分布
d = tf.random.normal([2, 2], mean=0.5, stddev=1)
# 截断式正态分布
e = tf.random.truncated_normal([2, 2], mean=0.5, stddev=1)

print("d:", d)
print("e:", e)
