# 闭包，计算n次幂
def nth_power(exp):
    def exponent_of(base):
        return base ** exp

    return exponent_of


if __name__ == '__main__':
    square = nth_power(2)
    cube = nth_power(3)

    print(square(2))
    print(cube(2))
    print(square(2))
    print(cube(2))
