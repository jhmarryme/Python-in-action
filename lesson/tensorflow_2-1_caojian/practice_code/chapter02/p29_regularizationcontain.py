# 导入所需模块
import numpy as np
import pandas as pd
import tensorflow as tf
from matplotlib import pyplot as plt

# 1. 数据读取与预处理
# 读入数据/标签 生成x_train y_train
# 使用pandas库的read_csv函数读取dot.csv文件，将其存储为DataFrame对象df
df = pd.read_csv('dot.csv')
# 提取特征列 'x1' 和 'x2' 作为特征数据，并转换为numpy数组
x_data = np.array(df[['x1', 'x2']])
# 提取标签列 'y_c' 作为标签数据，并转换为numpy数组
y_data = np.array(df['y_c'])

# 将特征数据作为训练特征
x_train = x_data
# 将标签数据重塑为列向量形式，以适应后续计算
y_train = y_data.reshape(-1, 1)

# 根据标签数据为每个样本分配颜色，用于后续可视化
# 如果标签为1则颜色为红色，为0则为蓝色
Y_c = [['red' if y else 'blue'] for y in y_train]
print(Y_c)
# 转换x的数据类型，否则后面矩阵相乘时会因数据类型问题报错
x_train = tf.cast(x_train, tf.float32)
y_train = tf.cast(y_train, tf.float32)

# from_tensor_slices函数切分传入的张量的第一个维度，生成相应的数据集，使输入特征和标签值一一对应集，
# 使输入特征和标签值一一对应，并将数据划分为大小为32的批次
train_db = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(32)

# 2. 神经网络参数定义
# 生成神经网络的参数，输入层为2个神经元（对应两个特征x1和x2），
# 隐藏层为11个神经元，1层隐藏层，输出层为1个神经元
# 用tf.Variable()保证参数可训练


# 初始化输入层到隐藏层的权重矩阵，形状为[2, 11]，从正态分布中随机采样
# 权重矩阵w1用于将输入层的2个特征映射到隐藏层的11个神经元
# 11是自己设定的，可根据实际情况调整
w1 = tf.Variable(tf.random.normal([2, 11]), dtype=tf.float32)
# 初始化隐藏层的偏置向量，形状为[11]，初始值为0.01
# 偏置b1用于给隐藏层的每个神经元添加一个固定的偏移量
b1 = tf.Variable(tf.constant(0.01, shape=[11]))

# 初始化隐藏层到输出层的权重矩阵，形状为[11, 1]，从正态分布中随机采样
# 权重矩阵w2用于将隐藏层的11个神经元的输出映射到输出层的1个神经元
w2 = tf.Variable(tf.random.normal([11, 1]), dtype=tf.float32)
# 初始化输出层的偏置向量，形状为[1]，初始值为0.01
# 偏置b2用于给输出层的神经元添加一个固定的偏移量
b2 = tf.Variable(tf.constant(0.01, shape=[1]))

# 设置学习率为0.01
# 学习率控制着参数更新的步长，过大可能导致模型无法收敛，过小则会使训练速度变慢
lr = 0.01
# 设置循环轮数为400
# 循环轮数表示模型对整个数据集进行训练的次数
epoch = 400

# 3. 训练部分
for epoch in range(epoch):
    for step, (x_train, y_train) in enumerate(train_db):
        # 使用tf.GradientTape()记录梯度信息，用于后续计算梯度
        # tf.GradientTape会自动跟踪在其上下文中执行的所有操作，方便后续计算梯度
        with tf.GradientTape() as tape:
            # 记录神经网络从输入层到隐藏层的乘加运算
            # 通过矩阵乘法将输入特征与权重矩阵w1相乘，再加上偏置b1
            h1 = tf.matmul(x_train, w1) + b1
            # 使用ReLU激活函数对隐藏层的输出进行非线性变换
            # ReLU函数可以引入非线性因素，增强模型的表达能力
            h1 = tf.nn.relu(h1)
            # 记录神经网络从隐藏层到输出层的乘加运算，得到预测值
            # 通过矩阵乘法将隐藏层的输出与权重矩阵w2相乘，再加上偏置b2
            y = tf.matmul(h1, w2) + b2

            # 采用均方误差损失函数mse = mean(sum(y-out)^2)
            # 计算预测值y与真实标签y_train之间的均方误差
            loss_mse = tf.reduce_mean(tf.square(y_train - y))
            # 添加l2正则化
            # 正则化用于防止模型过拟合，提高模型的泛化能力
            loss_regularization = []
            # tf.nn.l2_loss(w)=sum(w ** 2) / 2
            # 计算权重矩阵 w1/w2 的L2正则化损失
            loss_regularization.append(tf.nn.l2_loss(w1))
            loss_regularization.append(tf.nn.l2_loss(w2))
            # 求和
            # 例：x=tf.constant(([1,1,1],[1,1,1]))
            #   tf.reduce_sum(x)
            # >>>6
            # loss_regularization = tf.reduce_sum(tf.stack(loss_regularization))
            # 将w1和w2的L2正则化损失相加
            loss_regularization = tf.reduce_sum(loss_regularization)
            # 最终的损失函数为均方误差损失加上正则化损失乘以正则化系数0.03
            loss = loss_mse + 0.03 * loss_regularization  # REGULARIZER = 0.03

        # 计算loss对各个参数的梯度
        variables = [w1, b1, w2, b2]
        grads = tape.gradient(loss, variables)

        # 实现梯度更新
        # w1 = w1 - lr * w1_grad
        w1.assign_sub(lr * grads[0])
        b1.assign_sub(lr * grads[1])
        w2.assign_sub(lr * grads[2])
        b2.assign_sub(lr * grads[3])

    # 每200个epoch，打印loss信息
    if epoch % 20 == 0:
        print('epoch:', epoch, 'loss:', float(loss))

# 4. 预测部分
print("*******predict*******")
# xx在-3到3之间以步长为0.01，yy在-3到3之间以步长0.01,生成间隔数值点
# 使用numpy的mgrid函数生成二维网格坐标
xx, yy = np.mgrid[-3:3:.1, -3:3:.1]
# 将xx, yy拉直，并合并配对为二维张量，生成二维坐标点
# 将网格坐标转换为二维数组，方便输入到神经网络进行预测
grid = np.c_[xx.ravel(), yy.ravel()]
grid = tf.cast(grid, tf.float32)
print(grid.shape)
# 将网格坐标点喂入神经网络，进行预测，probs为输出
probs = []

for x_predict in grid:
    # 使用训练好的参数进行预测
    # 对网格中的每个点进行前向传播计算
    h1 = tf.matmul([x_predict], w1) + b1
    h1 = tf.nn.relu(h1)
    y = tf.matmul(h1, w2) + b2  # y为预测结果
    probs.append(y)

print("probs长度", len(probs))
# 取第0列给x1，取第1列给x2
# 从原始特征数据中提取x1和x2列
x1 = x_data[:, 0]
x2 = x_data[:, 1]
# probs的shape调整成xx的样子
# 将预测结果的形状调整为与网格坐标一致
probs = np.array(probs).reshape(xx.shape)
print("probs形状", probs.shape)
print(probs)
# 绘制散点图，根据标签颜色绘制原始数据点
plt.scatter(x1, x2, color=np.squeeze(Y_c))
# 把坐标xx yy和对应的值probs放入contour<[‘kɑntʊr]>函数，
# 给probs值为0.5的所有点上色  plt点show后 显示的是红蓝点的分界线
# 绘制等高线图，将预测概率为0.5的点连接起来，形成分类边界
plt.contour(xx, yy, probs, levels=[.5])
plt.show()

# 读入红蓝点，画出分割线，包含正则化
# 不清楚的数据，建议print出来查看
