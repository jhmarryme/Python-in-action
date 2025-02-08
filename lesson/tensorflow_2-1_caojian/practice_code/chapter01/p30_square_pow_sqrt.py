import tensorflow as tf

a = tf.constant([2.0, 3.0])

# 平方
square_result = tf.square(a)
print(f"平方结果: {square_result}")  # [4.0, 9.0]

# 次方运算
pow_result = tf.pow(a, 3)
print(f"次方运算结果: {pow_result}")  # [8.0, 27.0]

# 平方根
sqrt_result = tf.sqrt(a)
print(f"平方根结果: {sqrt_result}")  # [1.4142, 1.7320]