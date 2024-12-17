# 给定一个 list 和一个指定数字，求这个数字在 list 中的位置。
# 1. 常规实现
def index_normal(L, target):
    result = []
    for i, num in enumerate(L):
        if num == target:
            result.append(i)
    return result


print(index_normal([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2))


# 2. 使用生成器实现
def index_generator(L, target):
    for i, num in enumerate(L):
        if num == target:
            yield i


print(list(index_generator([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2)))
