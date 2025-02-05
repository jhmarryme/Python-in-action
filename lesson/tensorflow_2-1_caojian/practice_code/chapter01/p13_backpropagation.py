import tensorflow as tf

# 定义多个学习率和迭代次数对
lr_epoch_pairs = [(0.2, 40), (0.001, 100), (0.999, 20)]

# 自定义w的初始值
initial_w = 5  # 你可以在这里修改w的初始值

# 遍历每个学习率和迭代次数对
for lr, epoch in lr_epoch_pairs:
    # 初始化变量w，初始值为自定义值，数据类型为float32
    w = tf.Variable(tf.constant(initial_w, dtype=tf.float32))

    # 打印开始训练的信息
    print(f"Started training with lr={lr}, initial w={initial_w}, and epoch={epoch}")
    print("-" * 50)

    # 开始迭代
    for epoch in range(epoch):
        with tf.GradientTape() as tape:
            # 定义损失函数为(w + 1)的平方
            loss = tf.square(w + 1)

        # 计算损失函数关于变量w的梯度
        grads = tape.gradient(loss, w)
        # 使用梯度下降算法更新变量w，即w = w - lr * grads
        w.assign_sub(lr * grads)
        # 打印当前迭代次数、变量w的值和损失函数的值
        print(f"Epoch {epoch + 1} with lr={lr}: w={w.numpy():.4f}, loss={loss:.4f}")

    # 打印最终结果
    print(f"Final result with lr={lr}: w={w.numpy():.4f}, loss={loss:.4f}")

    # 打印结束训练的信息
    print("-" * 50)
    print(f"Finished training with lr={lr}, initial w={initial_w}, and epoch={epoch + 1}")
    print("-" * 50)

# 最终目的：找到 loss 最小 即 w = -1 的最优参数w