import numpy as np
import tensorflow as tf

# 1. 生成训练数据
SEED = 23455
# 创建随机数生成器，种子为SEED，用于生成[0, 1)之间的随机数
rdm = np.random.RandomState(SEED)
# 生成包含32个样本，每个样本有2个特征的数据集x，数据在[0, 1)之间
x = rdm.rand(32, 2)
# 目标值计算公式 y = x1 + x2 + 噪声。
# 生成真实值y_，对于每个样本(x1, x2)，y_ = x1 + x2 + 噪声，噪声范围在[-0.05, 0.05]
# 噪声[0,1)/10=[0,0.1); [0,0.1)-0.05=[-0.05,0.05)
y_ = [[x1 + x2 + (rdm.rand() / 10.0 - 0.05)] for x1, x2 in x]
# print(y_)
x = tf.cast(x, dtype=tf.float32)

# 2. 初始化权重参数
# 定义权重变量w1，形状为[2, 1]，从标准差为1的正态分布中随机初始化，设置种子为1保证可复现
w1 = tf.Variable(initial_value=tf.random.normal(shape=[2, 1], stddev=1, seed=1))

# 3. 设定训练参数
epochs = 15000  # 训练轮数
lr = 0.002  # 学习率

# 4. 训练模型
for epoch in range(epochs):
    # 使用GradientTape记录计算图，以便后续计算梯度
    with tf.GradientTape() as tape:
        # 通过矩阵乘法计算预测值y，即y = x * w1
        y = tf.matmul(x, w1)
        # print(y.shape)
        # print(y)
        # 将y_转换为TensorFlow张量
        y__ = tf.convert_to_tensor(y_)
        # print(y__.shape)
        # 计算均方误差损失，即loss_mse = 1/n * sum((y_ - y) ** 2)
        loss_mse = tf.reduce_mean(tf.square(tf.subtract(y_, y)))
    # 计算损失函数loss_mse关于权重w1的梯度
    grads = tape.gradient(loss_mse, w1)
    # 更新权重w1，w1 = w1 - lr * grads
    w1.assign_sub(lr * grads)
    if epoch % 500 == 0:
        print(f"After {epoch} training steps,  loss is {loss_mse.numpy()}， w1 is {w1.numpy()}")

# 5. 打印最终的权重w1的值
print(f"Final w1 is: {w1.numpy()}")
