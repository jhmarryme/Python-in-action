if __name__ == '__main__':
    # 多个参数传递给装饰器
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("装饰器")
            func(*args, **kwargs)

        return wrapper


    @my_decorator
    def greet(index, name, message):
        print(str(index) + " 你好 " + name + '  ' + message)


    greet(1, 'xxx', 'yyy')
