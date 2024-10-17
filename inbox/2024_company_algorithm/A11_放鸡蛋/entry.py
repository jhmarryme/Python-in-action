"""
把M个同样的鸡蛋放在N个同样的篮子里，允许有的篮子空着不放，假设一个篮子的容量无限大，问共有多少种不同的分法？ 注意：5，1，1和1，5，1 是同一种分法。

输入
数字m: 鸡蛋总数
数字n: 篮子总数

输出
数字，总共有多少中不同的分法

输入样例
m = 7
n = 3
输出样例

8
"""

# 解答正确
def plan(m, n):
    # 创建一个 (m+1) x (n+1) 的二维DP表
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化基准情况：将0个鸡蛋分配到任意数量的篮子中，只有一种方法（所有篮子为空）
    for j in range(n + 1):
        dp[0][j] = 1

    # 填充DP表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if j > i:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - j][j]

    return dp[m][n]


# 示例输入
m = 7
n = 3

# 计算并输出结果
print(plan(m, n))
