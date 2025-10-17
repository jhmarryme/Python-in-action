import sys


def dijkstra_matrix(graph, start):
    n = len(graph)
    visited = [False] * n
    dist = [sys.maxsize] * n
    dist[start] = 0
    # 找到距离最近且未被访问过的节点u
    for _ in range(n):
        min_dist = sys.maxsize
        u = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        # 从寻找未被访问过且与u相连的边v, 若dist[u] + graph[u][v] < dist[v], 则更新v
        for v in range(n):
            if not visited[v] and graph[u][v] > 0 and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
    return dist
    pass


def test_dijkstra_matrix():
    # 测试用例1：简单有向图
    graph1 = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]
    start1 = 0
    result1 = dijkstra_matrix(graph1, start1)
    print(f"邻接矩阵测试用例1结果: \n{result1}")
    print(f"预期结果:\n[0, 4, 12, 19, 21, 11, 9, 8, 14]\n")

    # 测试用例2：包含不可达节点
    graph2 = [
        [0, 2, 0, 0],
        [0, 0, 3, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0]
    ]
    start2 = 0
    result2 = dijkstra_matrix(graph2, start2)
    print(f"邻接矩阵测试用例2结果: \n{result2}")
    print(f"预期结果:\n[0, 2, 5, {sys.maxsize}]\n")

    graph3 = [
        [0, 10, 0, 4, 0, 0],
        [10, 0, 8, 2, 6, 0],
        [0, 8, 10, 15, 1, 5],
        [4, 2, 15, 0, 6, 0],
        [0, 6, 1, 6, 0, 12],
        [0, 0, 5, 0, 12, 0]
    ]

    start3 = 0
    result3 = dijkstra_matrix(graph3, start3)
    print(f"邻接矩阵测试用例2结果: \n{result3}")
    print(f"预期结果:\n[0, 6, 11, 4, 10, 16]\n")


test_dijkstra_matrix()
