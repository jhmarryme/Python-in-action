'''
我希望您能够充当算法工程师，使用python解答算法题。给出可运行在codeCampus上的嗯代码，并提供解题思路。
需要最高优先级保证代码的正确性，同时尽可能多的考虑多种输入的运行情况。
题目信息如下：

有一个M*N二维迷宫, 出口只有一个, 在迷宫最右下角, 即迷宫的最后一个格子,入口也只有一个, 在迷宫最左上角, 即迷宫的第一个格子

每次只能向左或者向下移动一格，不能向后或者向上移动，
算出有多少条不同的路径可以到达出口

输入
两个数字M和N，M表示迷宫有多少行小格，N表示迷宫有多少列小格。

输出
不同的路径数量

输入样例
M=3, N=3

输出样例
6

函数定义风格如下:
def find_path_number(m: int, n: int) -> int:
    return 0


'''
# 部分正确, 存在错误和超时
import math

def find_path_number(m: int, n: int) -> str:
    """
    计算令狐冲从左上角移动到右下角的不同路径数量。
    仅能向右或向下移动一格。

    参数:
    - m (int): 网格的行数。
    - n (int): 网格的列数。

    返回:
    - str: 不同路径数量的字符串表示。
    """
    # 边界情况处理
    if m <= 0 or n <= 0:
        return "0"

    # 使用组合数学公式计算路径数量
    total_steps = (m - 1) + (n - 1)
    steps_down = m - 1
    try:
        # math.comb 是从 Python 3.10 开始支持的
        path_count = math.comb(total_steps, steps_down)
    except AttributeError:
        # 如果使用的是 Python 3.9 或更低版本，手动计算组合数
        def comb(n, k):
            if k < 0 or k > n:
                return 0
            if k == 0 or k == n:
                return 1
            k = min(k, n - k)  # 利用组合数对称性
            result = 1
            for i in range(1, k + 1):
                result = result * (n - k + i) // i
            return result
        path_count = comb(total_steps, steps_down)

    return str(path_count)

# =========================
# Example Test Cases
# =========================
if __name__ == "__main__":
    # Test Case 1: Sample Input 1
    m1, n1 = 3, 3
    print(find_path_number(m1, n1))  # Expected Output: "6"

    # Test Case 2: Single Row
    m2, n2 = 1, 5
    print(find_path_number(m2, n2))  # Expected Output: "1"

    # Test Case 3: Single Column
    m3, n3 = 5, 1
    print(find_path_number(m3, n3))  # Expected Output: "1"

    # Test Case 4: Larger Grid
    m4, n4 = 10, 10
    print(find_path_number(m4, n4))  # Expected Output: "48620"

    # Test Case 5: Minimal Grid
    m5, n5 = 1, 1
    print(find_path_number(m5, n5))  # Expected Output: "1"

    # Test Case 6: Asymmetric Grid
    m6, n6 = 4, 5
    print(find_path_number(m6, n6))  # Expected Output: "35"

    # Test Case 7: Large Grid
    m7, n7 = 1000, 1000
    # Note: The number will be extremely large and may not display fully.
    # Uncomment the following line to test (may consume significant memory and time)
    # print(find_path_number(m7, n7))