import functools

if __name__ == '__main__':
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('wrapper of decorator')
            func(*args, **kwargs)

        return wrapper


    @my_decorator
    def greet(message):
        print(message)


    greet('hello world')
    print(greet.__name__)
