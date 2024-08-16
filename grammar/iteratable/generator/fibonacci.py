def fibonacci(n):
    """斐波那契数列实现"""
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
        yield a


# 获取斐波那契数列前 10 个成员
fibonacci_ = fibonacci(10)
for i in fibonacci_:
    print(i)
