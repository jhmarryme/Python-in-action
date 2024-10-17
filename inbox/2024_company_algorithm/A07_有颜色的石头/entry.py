"""
有颜色的石头
描述
你有一排石头，共有m个，每个石头有k种颜色中的一种。为了使任意两种相同颜色的石头之间不再有其他颜色的石头隔开，你最少需要移除多少个石头？

输入
数字m: 石头总数，数字k： 颜色总数，其中1 ≤ m ≤ 100且1 ≤ k ≤ 5，石头颜色排列数组a： [A1,A2,A3,...,Am]，A1～Am的值来自集合{1, …, k}，表示k种不同的石头颜色。

输出
对于每个输入用例，程序应输出为了满足题目中给出的条件所需移除的最少石头数量。

输入样例
m = 10
k = 3
a = [2, 1, 2 ,2 ,1 ,1, 3 ,1 ,3, 3]

输出样例
2

函数定义风格如下:
def removeStones(m, k, inArr):
    return 1

"""
# 答案正确
def removeStones(m, k, inArr):
    from itertools import permutations

    # 初始化每种颜色的前缀和
    # prefix[c][j] 表示颜色 c 在前 j 个石头中出现的次数
    prefix = [[0]*(m+1) for _ in range(k+1)]  # 颜色从 1 到 k
    for c in range(1, k+1):
        for j in range(1, m+1):
            prefix[c][j] = prefix[c][j-1] + (1 if inArr[j-1] == c else 0)

    max_kept = 0

    colors = list(range(1, k+1))
    for perm in permutations(colors):
        # 初始化 DP 数组
        # dp[i][j] 表示前 i 种颜色在前 j 个石头中保留下来的最大石头数
        dp = [[0]*(m+1) for _ in range(k+1)]

        for i in range(1, k+1):
            current_color = perm[i-1]
            for j in range(1, m+1):
                # 对于当前颜色，尝试所有可能的分割点 l
                # 保留从 l+1 到 j 的当前颜色石头数
                # 并与之前的 dp[i-1][l] 相加
                max_val = 0
                for l in range(0, j+1):
                    val = dp[i-1][l] + (prefix[current_color][j] - prefix[current_color][l])
                    if val > max_val:
                        max_val = val
                dp[i][j] = max_val
        # 更新保留的最大石头数
        if dp[k][m] > max_kept:
            max_kept = dp[k][m]

    return m - max_kept

# 示例 1
m1 = 10
k1 = 3
a1 = [2, 1, 2, 2, 1, 1, 3, 1, 3, 3]
print(removeStones(m1, k1, a1))  # 输出: 2

# 示例 2
m2 = 5
k2 = 3
a2 = [2, 1, 2, 2, 1]
print(removeStones(m2, k2, a2))  # 输出: 1

# 示例 3
m3 = 10
k3 = 2
a3 = [2, 1, 2, 1, 2, 2, 1, 2, 2, 2]
print(removeStones(m3, k3, a3))  # 输出: 3