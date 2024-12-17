# 判断一个对象是否可迭代
from collections.abc import Iterable


def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False


params = [
    1234,
    '1234',
    [1, 2, 3, 4],
    set([1, 2, 3, 4]),
    {1: 1, 2: 2, 3: 3, 4: 4},
    (1, 2, 3, 4)
]
for param in params:
    print("{} is iterable? {}".format(param, is_iterable(param)))
print('---------------')
for param in params:
    print("{} is iterable? {}".format(param, isinstance(param, Iterable)))
