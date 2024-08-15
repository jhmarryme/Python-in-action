if __name__ == '__main__':
    # 单个参数传递给装饰器
    def my_decorator(func):
        def wrapper(message):
            print("装饰器")
            func(message)

        return wrapper


    @my_decorator
    def greet(message):
        print("你好 " + message)


    greet('xxx')
