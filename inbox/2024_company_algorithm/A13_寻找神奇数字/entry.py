'''
寻找神奇数字
描述

找出所有十进制表示下的四位数，这些数满足特性：

1.范围： 2992 =< n <=9999
2.它们四个数字的和等于它们在十六进制表示下数字的和，也等于它们在十二进制表示下数字的和。
例如，数字2991（十进制）的数字之和为2+9+9+1=21。它的十二进制表示为1893，这些数字加起来也是1+8+9+3=21。但是在十六进制中2991表示为BAF，而11+10+15=36，因此2991不满足特征。
然而，下一个数（2992）在所有三种表示方式中的数字之和都是22，所以2992满足特征。

输入
无

输出
数组，满足上述条件的所有数字，需要从小到大排序

输入样例 1
无
输出样例 1
[2992,2993, ... ]

函数定义风格如下:
def findNumber():
    return []


'''
def findNumber():
    def sum_of_digits(n, base):
        """计算数字n在指定base下的各位数字之和"""
        total = 0
        while n > 0:
            total += n % base
            n = n // base
        return total

    result = []
    for n in range(2992, 10000):
        sum_dec = sum_of_digits(n, 10)
        sum_bin = sum_of_digits(n, 12)
        sum_hex = sum_of_digits(n, 16)
        if sum_dec == sum_bin == sum_hex:
            result.append(n)
    return result

# 示例输出
print(findNumber())