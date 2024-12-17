if __name__ == "__main__":
    a = 2
    b = 2
    print(a == b)
    print(a is b)
    print("id(a) = {}".format(id(a)))
    print("id(b) = {}".format(id(b)))
    # 以上只对-5至256的值有效
    print('----------------')
    # python解释器中，a is b = false，pycharm运行true
    a = 10000000
    b = 10000000
    print(a == b)
    print(a is b)
    print("id(a) = {}".format(id(a)))
    print("id(b) = {}".format(id(b)))

    print('----------------')
    # 对于不可变变量
    t1 = (1, 2, [3, 4])
    t2 = (1, 2, [3, 4])
    print(t1 == t2)
    print(id(t1), id(t2))
    t1[-1].append(5)
    print(t1 == t2)
    print(id(t1), id(t2))
