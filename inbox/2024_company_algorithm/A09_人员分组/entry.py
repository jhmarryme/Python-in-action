"""
人员分组
描述

假设小组内有n个人，他们的年龄未知。
我们有一些关于他们的信息。包含在二维数组内：一共有m行，每行包含两个整数c和d, 表示第c个人的年龄大于等于第d个人的年龄
如二维数组：
[
[1 2]
[1 3]
]
表示第1个人的年龄大于第2个人，第1个人的年龄大于第3个人。
在同一组内，任何人的年龄都不能直接或间接地与其他人的年龄进行比较。每个人必须被分配到且仅能被分配到一个组。请计算出满足要求的最小分组数。

输入
数字n：表示组内总人数 （1=<n<=100000）
数字m：表示信息条数 （1=<m<=300000）
二维数组a：一共有m行，每行包含两个整数Si和Ti, 表示第Si个人的年龄大于等于第Ti个人的年龄

输出
输出一行，表示满足要求的最小分组数

输入样例
n=4
m=4
a=[
[1 2]
[1 3]
[2 4]
[3 4]
]
输出样例
3

函数定义风格如下:
def group(n, m, a):
return 0
"""


# 部分正确, 6分, 缺4
def group(n, m, a):
    from collections import deque

    # 创建邻接表和入度数组
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    for relation in a:
        s, t = relation
        adj[s].append(t)
        in_degree[t] += 1

    # 初始化队列，存储入度为0的节点
    queue = deque()
    # dp[i] 表示到达节点 i 的最长路径长度
    dp = [1] * (n + 1)
    for node in range(1, n + 1):
        if in_degree[node] == 0:
            queue.append(node)

    processed = 0  # 记录处理的节点数量
    while queue:
        current = queue.popleft()
        processed += 1
        for neighbor in adj[current]:
            if dp[neighbor] < dp[current] + 1:
                dp[neighbor] = dp[current] + 1
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if processed != n:
        # 存在环，无法形成DAG
        return -1

    return max(dp)


# 测试样例
n = 4
m = 4
a = [
    [1, 2],
    [1, 3],
    [2, 4],
    [3, 4]
]
print(group(n, m, a))  # 输出应为3
