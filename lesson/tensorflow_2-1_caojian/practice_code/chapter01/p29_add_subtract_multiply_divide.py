import tensorflow as tf

a = tf.constant([1, 2])
b = tf.constant([3, 4])

# 加法
add_result1 = tf.add(a, b)
add_result2 = a + b
print(f"加法（函数形式）: {add_result1}")
print(f"加法（运算符形式）: {add_result2}")

# 减法
sub_result1 = tf.subtract(a, b)
sub_result2 = a - b
print(f"减法（函数形式）: {sub_result1}")
print(f"减法（运算符形式）: {sub_result2}")

# 乘法
mul_result1 = tf.multiply(a, b)
mul_result2 = a * b
print(f"乘法（函数形式）: {mul_result1}")
print(f"乘法（运算符形式）: {mul_result2}")

# 除法
div_result1 = tf.divide(a, b)
div_result2 = a / b
print(f"除法（函数形式）: {div_result1}")
print(f"除法（运算符形式）: {div_result2}")