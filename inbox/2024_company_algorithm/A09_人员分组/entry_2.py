"""
我希望您能够充当算法工程师，使用python解答算法题。给出可运行在codeCampus上的嗯代码，并提供解题思路。
需要最高优先级保证代码的正确性，同时尽可能多的考虑多种输入的运行情况。
题目信息如下：

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
from collections import defaultdict, deque

def group(n, m, a):
    # 构建有向图
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)  # 节点的入度

    # 填充图和入度表
    for c, d in a:
        graph[c].append(d)
        in_degree[d] += 1

    # 使用拓扑排序，计算最小分组数
    # 拓扑排序所需队列
    queue = deque()
    # 存放每个节点的拓扑排序深度
    depth = [0] * (n + 1)

    # 将所有入度为0的节点加入队列
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            depth[i] = 1  # 初始深度为1（表示起点的第一组）

    # 进行拓扑排序
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
            # 更新拓扑深度
            depth[neighbor] = max(depth[neighbor], depth[node] + 1)

    # 输出最大深度值，即为最少分组数
    return max(depth)

# 测试用例
n = 4
m = 4
a = [
    [1, 2],
    [1, 3],
    [2, 4],
    [3, 4]
]
print(group(n, m, a))  # 输出应为 3
