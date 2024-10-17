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
现在我们需要将这N个人分成若干组，在同一组内，任何人的年龄都不能直接或间接地与其他人的年龄进行比较。每个人必须被分配到且仅能被分配到一个组。
请计算出满足要求的最小分组数。

输入
数字n：表示组内总人数 （1=<n<=100000）
数字m：表示信息条数 （1=<m<=300000）
二维数组a：一共有m行，每行包含两个整数Si和Ti, 表示第Si个人的年龄大于等于第Ti个人的年龄

输出
输出一行，表示满足要求的最小分组数,如果没有满足要求的分组，返回0

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
from collections import deque, defaultdict


def group(n, m, a):
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)

    for u, v in a:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque()
    group_level = [0] * (n + 1)

    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            group_level[i] = 1

    processed_count = 0

    while queue:
        node = queue.popleft()
        processed_count += 1

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
            group_level[neighbor] = max(group_level[neighbor], group_level[node] + 1)

    if processed_count != n:
        return 0

    return max(group_level)


# 测试样例
n = 4
m = 4
a = [
    [1, 2],
    [1, 3],
    [2, 4],
    [3, 4]
]

print(group(n, m, a))  # 输出 3
