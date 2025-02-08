import tensorflow as tf

# 定义一个可训练变量
x = tf.Variable(tf.constant(3.0))

# 创建 GradientTape 上下文管理器
with tf.GradientTape() as tape:
    # 定义需要求导的函数
    y = tf.pow(x, 2)

# 计算 y 关于 x 的梯度
dy_dx = tape.gradient(y, x)
print(f"y = x^2 在 x = 3 处的梯度: {dy_dx.numpy()}")
