import numpy as np
import tensorflow as tf

# # 创建一个NumPy数组a，其值为从0到4的整数序列
a = np.arange(0, 5)
# 将 numpy 的数据类型转换为 Tensor 数据类型
# tf.convert_to_tensor (数据名，dtype = 数据类型 (可选))
b = tf.convert_to_tensor(a, dtype=tf.int64)
print("a:", a)
print("b:", b)
