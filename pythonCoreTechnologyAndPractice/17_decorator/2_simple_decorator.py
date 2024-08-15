if __name__ == '__main__':
    # 简单装饰器例子
    def my_decorator(func):
        def wrapper():
            print("装饰器")
            func()

        return wrapper


    def greet():
        print("你好")


    @my_decorator
    def greet2():
        print("你好")


    greet = my_decorator(greet)
    greet()
    print('-----------')
    greet2()
