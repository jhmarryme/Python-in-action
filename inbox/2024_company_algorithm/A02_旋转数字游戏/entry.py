'''
旋转数字游戏
描述

小明与爸爸在玩一个数字游戏，小明按照以下顺序排列0-9个数字：

   0   1   2   3   4
   5   6   7   8   5
   4   3   4   9   6
   3   2   1   0   7
   2   1   0   9   8
即从左上角开始旋转的依次重复排列0-9这10个数字，当完成一圈之后，从里面一圈开始再重复


小明只需要告诉爸爸他排列的数字矩阵是几行几列，然后让爸爸算出第n行的数字从左到右依次是哪几个数字。

例如，例子中，小明需要告诉爸爸他排列的是5行6列，让爸爸告诉他第2行从左向右依次是哪几个数字，爸爸得告诉小明，从第2行从左向右的数字依次是7、8、9、0、1、6。
当小明说的行数和列数越来越大时，小明的爸爸就计算不过来了，现在他需要你帮忙写一段程序来帮忙计算一下这个游戏的结果。

输入
数字排列的行数n、列数m和猜数字的行数k, n和m都是大于0且不大于100000的的自然数，1<=k<=n。

输出
第k行的从左向右的数字序列组成的字符串s。

输入样例 1
n=5,m=6,k=3
输出样例 1
s = "678927"

函数定义风格如下:
def solve(n: int, m: int, k: int) -> str:
    return ""

'''


# 答案正确

def solve(n: int, m: int, k: int) -> str:
    digits_in_row = []

    for j in range(1, m + 1):
        L = min(k - 1, j - 1, n - k, m - j)
        S = L * (2 * n + 2 * m - 4 * L)

        w = m - 2 * L  # Width
        h = n - 2 * L  # Height

        if k == L + 1:
            P = j - (L + 1)
        elif j == m - L:
            P = (w - 1) + (k - (L + 1))
        elif k == n - L:
            P = (w - 1) + (h - 1) + (m - L - j)
        elif j == L + 1:
            P = 2 * (w - 1) + (h - 1) + (n - L - k)
        else:
            P = 0

        step = S + P
        digit = step % 10
        digits_in_row.append(str(digit))

    s = ''.join(digits_in_row)

    return s


# =============================
# Example Test Cases
# =============================
if __name__ == "__main__":
    # Test Case 1: Sample Input 1
    n1, m1, k1 = 5, 6, 3
    print(solve(n1, m1, k1))  # Expected Output: "678927"

    # Test Case 2: Single Row
    n2, m2, k2 = 1, 5, 1
    print(solve(n2, m2, k2))  # Expected Output: "01234"

    # Test Case 3: Single Column
    n3, m3, k3 = 5, 1, 3
    print(solve(n3, m3, k3))  # Expected Output: "2"

    # Test Case 4: Larger Grid
    n4, m4, k4 = 10, 10, 5
    print(solve(n4, m4, k4))  # Expected Output: Depends on spiral filling

    # Test Case 5: Minimal Grid
    n5, m5, k5 = 1, 1, 1
    print(solve(n5, m5, k5))  # Expected Output: "0"

    # Test Case 6: Asymmetric Grid
    n6, m6, k6 = 4, 5, 2
    print(solve(n6, m6, k6))  # Expected Output: Depends on spiral filling

    # Additional Test Case 7: Edge Case with k exceeding grid bounds
    # Not applicable since k <=n as per input constraints

    # Additional Test Case 8: Large Grid (n and m up to 100,000)
    # Note: Uncomment the following lines to test with large inputs
    # n7, m7, k7 = 100000, 100000, 50000
    # print(solve(n7, m7, k7))  # Expected Output: Depends on spiral filling

    # Additional Test Case 9: Middle Layer in Odd-sized Grid
    n9, m9, k9 = 7, 7, 4
    print(solve(n9, m9, k9))  # Expected Output: Depends on spiral filling
