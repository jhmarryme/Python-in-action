import sys


def dijkstra_adjacency_list(graph, start):
    n = len(graph)
    dist = [sys.maxsize] * n
    visited = [False] * n
    dist[start] = 0
    for _ in range(n):
        u = -1
        min_dist = sys.maxsize
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        for element in graph[u]:
            x, y = element[0], element[1]
            if not visited[x] and dist[u] + y < dist[x]:
                dist[x] = dist[u] + y
    return dist


def test_dijkstra_adjacency_list():
    # 测试用例1：与邻接矩阵测试用例1相同的图
    graph1 = [
        [(1, 4), (7, 8)],
        [(0, 4), (2, 8), (7, 11)],
        [(1, 8), (3, 7), (5, 4), (8, 2)],
        [(2, 7), (4, 9), (5, 14)],
        [(3, 9), (5, 10)],
        [(2, 4), (3, 14), (4, 10), (6, 2)],
        [(5, 2), (7, 1), (8, 6)],
        [(0, 8), (1, 11), (6, 1), (8, 7)],
        [(2, 2), (6, 6), (7, 7)]
    ]
    start1 = 0
    result1 = dijkstra_adjacency_list(graph1, start1)
    print(f"邻接表测试用例1结果: {result1}")
    print(f"预期结果: [0, 4, 12, 19, 21, 11, 9, 8, 14]\n")

    # 测试用例2：简单无向图
    graph2 = [
        [(1, 2), (3, 6)],
        [(0, 2), (2, 3), (3, 8), (4, 5)],
        [(1, 3), (4, 7)],
        [(0, 6), (1, 8)],
        [(1, 5), (2, 7)]
    ]
    start2 = 0
    result2 = dijkstra_adjacency_list(graph2, start2)
    print(f"邻接表测试用例2结果: {result2}")
    print(f"预期结果: [0, 2, 5, 6, 7]\n")
test_dijkstra_adjacency_list()