
def find_path_number(m: int, n: int) -> int:
    dp = [0] * n
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[j] = 1
            else:
                dp[j] += dp[j - 1]
    return dp[n - 1]

# 测试样例
print(find_path_number(3, 3))  # 输出: 6

list = [0] * 6
list.insert(3, 1)
list.insert(5, 2)
print(list)