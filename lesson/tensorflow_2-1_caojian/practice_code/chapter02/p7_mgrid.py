import numpy as np

# 使用 np.mgrid 生成网格矩阵
grid = np.mgrid[0:2:1, 3:7:1]

# 打印输出的形状
print("输出形状:", grid.shape)

# 打印生成的网格矩阵
print("生成的网格矩阵:\n", grid)

# 生成等间隔数值点
x, y = np.mgrid[1:3:1, 2:4:0.5]
# 将x, y拉直，并合并配对为二维张量，生成二维坐标点
grid = np.c_[x.ravel(), y.ravel()]
print("x:\n", x)
print("y:\n", y)
print("x.ravel():\n", x.ravel())
print("y.ravel():\n", y.ravel())
print('grid:\n', grid)
