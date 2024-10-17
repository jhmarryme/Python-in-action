def find_path_number(m: int, n: int) -> str:
    dp = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]

    return f"P={dp[-1]}"

# 测试样例
print(find_path_number(3, 3))  # 输出: P=6
