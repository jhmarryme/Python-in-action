# 请记住，'type'实际上是一个类，就像'str'和'int'一样
# 所以，你可以从type继承
class MetaA(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(cls, name, bases, dct):
        print('MetaA.__new__')
        # 这种方式不会调用__init__方法
        # return type(name, bases, dct)
        # 这种方式会调用__init__
        return type.__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print('MetaA.__init__')


class A(object, metaclass=MetaA):
    pass


print(A())
