import numpy as np
import tensorflow as tf

SEED = 23455
COST = 1
PROFIT = 99

rdm = np.random.RandomState(SEED)
x = rdm.rand(32, 2)
y_ = [[x1 + x2 + (rdm.rand() / 10.0 - 0.05)] for x1, x2 in x]
x = tf.cast(x, dtype=tf.float32)

w1 = tf.Variable(initial_value=tf.random.normal(shape=[2, 1], stddev=1, seed=1))

epochs = 10000
lr = 0.002

for epoch in range(epochs):
    with tf.GradientTape() as tape:
        y = tf.matmul(x, w1)
        loss_custom = tf.reduce_sum(tf.where(tf.greater(y, y_), (y - y_) * COST, (y_ - y) * PROFIT))
    grads = tape.gradient(loss_custom, w1)
    w1.assign_sub(lr * grads)
    if epoch % 500 == 0:
        print(f"After {epoch} training steps,  loss is {loss_custom.numpy()}， w1 is {w1.numpy()}")

print(f"Final w1 is: {w1.numpy()}")

# 自定义损失函数
# 酸奶成本1元， 酸奶利润99元
# 成本很低，利润很高，人们希望多预测些，生成模型系数大于1，往多了预测
