# 思考题
class A():
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        A.__init__(self)
        print("B")


class C(A):
    def __init__(self):
        A.__init__(self)
        print("C")


class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print("D")


if __name__ == '__main__':
    d = D()
