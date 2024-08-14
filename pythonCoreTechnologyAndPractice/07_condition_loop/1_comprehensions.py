# 绘制 y = 2*|x| + 5 的函数图像，给定集合 x 的数据点，需要计算出 y 的数据集合
def function1():
    list = [1, 2, 3, -1, -2, -3]
    # y = 2*|x| + 5
    y = [2 * x + 5 if x > 0 else 2 * (-x) + 5 for x in list]
    print(y)
    # y = 2*x + 5 ( if x > 0)
    y = [2 * x + 5 for x in list if x > 0]
    print(y)


# 按逗号分割单词，去掉首位的空字符，并过滤掉长度小于等于 3 的单词，最后返回由单词组成的列表。
def function2():
    global text
    text = ' Today, is, Sunday'
    text_list = [s.strip() for s in text.split(",") if len(s) > 3]
    print(text_list)


if __name__ == '__main__':
    function1()
    function2()
