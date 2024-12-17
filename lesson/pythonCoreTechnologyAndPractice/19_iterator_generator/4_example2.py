# 给定两个有序序列，判断第一个是不是第二个的子序列

# 1. 通过生成器实现
def is_subsequence(a, b):
    b = iter(b)
    return all(i in b for i in a)


print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))

print('----------')


# 2. 常规方法实现, 将上面的代码复杂化
def is_subsequence2(a, b):
    b = iter(b)
    print(b)

    gen = (i for i in a)
    print(gen)

    for i in gen:
        print(i)

    gen = ((i in b) for i in a)
    print(gen)

    for i in gen:
        print(i)

    return all((i in b) for i in a)


print(is_subsequence2([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence2([1, 4, 3], [1, 2, 3, 4, 5]))
