if __name__ == '__main__':
    # 函数作为变量
    def func(message):
        print("收到一个消息:{}".format(message))


    send_message = func
    send_message("hello world")


    # 函数作为参数
    def root_call(fun, message):
        print(fun(message))


    root_call(func, "函数参数")


    # 函数嵌套
    def fund(message):
        def get_message(message):
            print("收到一个消息:{}".format(message))

        return get_message(message)


    fund("函数嵌套")


    # 闭包
    def func_closure():
        def get_message(message):
            print("收到一个消息:{}".format(message))

        return get_message


    send_message = func_closure()
    send_message("返回函数对象(闭包)")
