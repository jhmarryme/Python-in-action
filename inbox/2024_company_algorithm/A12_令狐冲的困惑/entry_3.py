def find_path_number(m: int, n: int) -> str:
    """
    计算令狐冲从沼泽地带的左上角到达右下角出口的不同路径数量。
    每次只能向右或向下移动一格。

    参数:
    m (int): 沼泽地带的行数。
    n (int): 沼泽地带的列数。

    返回:
    str: 不同的路径数量。
    """
    if m <= 0 or n <= 0:
        return "0"  # 行数或列数小于等于0无路径可行
    if m == 1 or n == 1:
        return "1"  # 只有一行或一列，只有一条路径

    # 初始化dp数组
    dp = [[0] * n for _ in range(m)]

    # 设置起点
    dp[0][0] = 1

    # 填充第一行
    for j in range(1, n):
        dp[0][j] = 1  # 第一行只有一种路径

    # 填充第一列
    for i in range(1, m):
        dp[i][0] = 1  # 第一列只有一种路径

    # 填充其余的dp表
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return str(dp[m - 1][n - 1])  # 返回右下角的路径数

# 示例测试
if __name__ == "__main__":
    print(find_path_number(3, 3))  # 输出: "6"
    print(find_path_number(1, 5))  # 输出: "1"
    print(find_path_number(2, 2))  # 输出: "2"
    print(find_path_number(0, 5))  # 输出: "0"
    print(find_path_number(5, 5))  # 输出: "70"