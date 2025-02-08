import tensorflow as tf

matrix_a = tf.ones([3, 2])
matrix_b = tf.fill([2, 3], 3.)

# 矩阵乘法（两种形式）
matmul_result1 = tf.matmul(matrix_a, matrix_b)
matmul_result2 = matrix_a @ matrix_b
print(f"矩阵乘法（函数形式）: {matmul_result1}")
print(f"矩阵乘法（运算符形式）: {matmul_result2}")
