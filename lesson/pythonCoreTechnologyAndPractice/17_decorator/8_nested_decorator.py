# 装饰器嵌套
import functools


def my_decorator_a(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("functools的装饰器a")
        func(*args, **kwargs)

    return wrapper


def my_decorator_b(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("functools的装饰器b")
        func(*args, **kwargs)

    return wrapper


@my_decorator_a
@my_decorator_b
def greet3(message):
    print(message)


if __name__ == '__main__':
    greet3("functools")
    print(greet3.__name__)
    