# 实现一个迭代器类，返回偶数
class MyIterator:
    """
    迭代器类
    """

    # 类构造函数，调用时最先执行
    # 用于分配执行最初所需的任何值
    def __init__(self):
        self.num = 0

    # iter()和next()方法使这个类变成迭代器
    def __iter__(self):
        # 类本身就是迭代器，故直接返回本身
        return self

    def __next__(self):
        # 返回当前值
        return_num = self.num
        # 只要值大于等于6，就停止迭代
        if return_num >= 6:
            raise StopIteration
        # 并改变下一次调用的状态
        self.num += 2
        return return_num


my_iterator = MyIterator()

for value in my_iterator:
    print(value)
print('--------')

my_iterator = MyIterator().__iter__()
while True:
    try:
        my_num = next(my_iterator)
    except StopIteration:
        break
    print(my_num)
