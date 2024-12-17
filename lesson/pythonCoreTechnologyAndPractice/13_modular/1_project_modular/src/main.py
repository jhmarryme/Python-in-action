# 非pycharm Sources Root方式运行时， 可能会找不到根目录
# import sys
#
# sys.path.append("..")

from proto.mat import Matrix
from utils.mat_mul import mat_mul

if __name__ == '__main__':
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])
    print(mat_mul(a, b).data)
