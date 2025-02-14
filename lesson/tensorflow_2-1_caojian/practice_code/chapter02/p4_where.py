import tensorflow as tf

a = tf.constant([1, 2, 3])
b = tf.constant([4, 5, 6])
condition = tf.greater(a, b)  # 比较 a 和 b 的元素大小
result = tf.where(condition, a, b)
# 解释：若 a 中的元素大于 b 中对应位置的元素，返回 a 对应位置的元素，否则返回 b 对应位置的元素
# 打印结果将显示根据条件选择的元素
print(f"根据条件选择的元素为: {result.numpy()}")  # 输出示例: 根据条件选择的元素为: [4 5 6]
