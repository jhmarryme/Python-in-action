import copy

if __name__ == '__main__':
    # 浅拷贝
    l1 = [1, 2, 3]
    l2 = list(l1)
    print(l1 == l2)
    print(l1 is l2)
    s1 = set([1, 2, 3])
    s2 = set(s1)
    print(s1, s2)
    print(s1 == s2)
    print(s1 is s2)
    # 通过切片操作
    l1 = [1, 2, 3]
    l2 = l1[:]
    print(l1 == l2)
    print(l1 is l2)
    # 使用copy函数
    l2 = copy.copy(l1)
    print(l1 == l2)
    print(l1 is l2)
    # 元组的不同，返回一个指向元组的引用
    t1 = (1, 2, 3)
    t2 = tuple(t1)
    print(t1 == t2)
    print(t1 is t2)

    # 浅拷贝的副作用
    l1 = [[1, 2], (30, 40)]
    l2 = list(l1)
    l1.append(100)
    l1[0].append(3)
    print(l1)
    print(l2)
    l1[1] += (50, 60)
    print(l1)
    print(l2)
