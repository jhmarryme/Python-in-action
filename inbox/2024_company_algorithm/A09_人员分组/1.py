from collections import defaultdict

def dfs(graph, node, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.append(node)

def reverse_graph(graph):
    reversed_graph = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            reversed_graph[v].append(u)
    return reversed_graph

def scc_dfs(reversed_graph, node, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in reversed_graph[node]:
        if not visited[neighbor]:
            scc_dfs(reversed_graph, neighbor, visited, component)

def kosaraju(n, edges):
    # 创建图
    graph = defaultdict(list)
    for c, d in edges:
        graph[c-1].append(d-1)  # 将索引调整为0-based

    # 第一次DFS填充栈
    visited = [False] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited, stack)

    # 反转图
    reversed_graph = reverse_graph(graph)

    # 重置visited数组
    visited = [False] * n
    scc_count = 0

    # 第二次DFS确定SCC
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            scc_dfs(reversed_graph, node, visited, component)
            scc_count += 1

    return scc_count

def group(n, m, a):
    # 调用Kosaraju算法计算强连通分量的数量
    return kosaraju(n, a)

# 示例测试
n = 4
m = 4
a = [
    [1, 2],
    [1, 3],
    [2, 4],
    [3, 4]
]
print(group(n, m, a))  # 应输出 3