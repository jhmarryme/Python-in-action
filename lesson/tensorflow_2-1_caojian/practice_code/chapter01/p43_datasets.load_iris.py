import pandas as pd
from pandas import DataFrame
from sklearn import datasets

# .data 属性返回的是一个二维数组，每一行代表一个样本，每一列代表一个特征
x_data = datasets.load_iris().data  # .data返回iris数据集所有输入特征

# .target 属性返回的是一个一维数组，每个元素代表对应样本的类别标签
y_data = datasets.load_iris().target  # .target返回iris数据集所有标签
print("x_data from datasets: \n", x_data)
print("y_data from datasets: \n", y_data)

x_data = DataFrame(x_data, columns=['花萼长度', '花萼宽度', '花瓣长度', '花瓣宽度'])  # 为表格增加行索引（左侧）和列标签（上方）
pd.set_option('display.unicode.east_asian_width', True)  # 设置列名对齐
print("x_data add index: \n", x_data)

x_data['类别'] = y_data  # 新加一列，列标签为‘类别’，数据为y_data
print("x_data add a column: \n", x_data)

# 类型维度不确定时，建议用print函数打印出来确认效果
