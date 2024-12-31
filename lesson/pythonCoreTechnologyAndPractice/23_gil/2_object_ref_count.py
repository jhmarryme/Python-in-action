import sys

a = []
b = a
# a 的引用计数是 3，因为有 a、b 和作为参数传递的 getrefcount 这三个地方，都引用了一个空列表
print(sys.getrefcount(a))
