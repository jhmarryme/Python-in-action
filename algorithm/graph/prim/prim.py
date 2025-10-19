import heapq


def prim(graph, start):
    size = len(graph)
    visited = [False] * size
    heap = []
    mst = []
    total_weight = 0

    visited[start] = True
    for v, weight in graph[start]:
        heapq.heappush(heap, (start, v, weight))

    while heap and len(mst) < size - 1:
        u, v, weight = heapq.heappop(heap)
        if not visited[v]:
            mst.append((u, v, weight))
            total_weight += weight
            visited[v] = True
            for v_next, weight_next in graph[v]:
                if not visited[v_next]:
                    heapq.heappush(heap, (v, v_next, weight_next))
    if len(mst) == size - 1:
        return mst, total_weight
    return None, 0


def test_mst_algorithms():
    # 测试用例1：经典连通图
    print("测试用例1：经典连通图")
    # 顶点0-4，边列表：(u, v, weight)
    edges1 = [
        (0, 1, 2), (0, 3, 6),
        (1, 2, 3), (1, 3, 8), (1, 4, 5),
        (2, 4, 7),
        (3, 4, 9)
    ]
    # 转换为邻接表（用于Prim）
    adj1 = [[] for _ in range(5)]
    for u, v, w in edges1:
        adj1[u].append((v, w))
        adj1[v].append((u, w))
    # Prim测试（从顶点0开始）
    prim_edges, prim_weight = prim(adj1, 0)
    print("Prim算法选中的边：", prim_edges)
    print("Prim算法总权重：", prim_weight)  # 预期：16
    print()

    # 测试用例2：含相同权重边的图
    print("测试用例2：含相同权重边的图")
    edges2 = [
        (0, 1, 1), (0, 2, 1),
        (1, 2, 1), (1, 3, 2),
        (2, 3, 2)
    ]
    adj2 = [[] for _ in range(4)]
    for u, v, w in edges2:
        adj2[u].append((v, w))
        adj2[v].append((u, w))
    prim_edges2, prim_weight2 = prim(adj2, 0)
    print("Prim算法选中的边：", prim_edges2)
    print("Prim算法总权重：", prim_weight2)  # 预期：4
    print()

    # 测试用例3：非连通图（无生成树）
    print("测试用例3：非连通图")
    edges3 = [
        (0, 1, 1), (1, 2, 2),  # 连通分量1
        (3, 4, 3)  # 连通分量2（与前者不连通）
    ]
    adj3 = [[] for _ in range(5)]
    for u, v, w in edges3:
        adj3[u].append((v, w))
        adj3[v].append((u, w))
    prim_edges3, _ = prim(adj3, 0)
    print("Prim算法结果：", "无生成树" if prim_edges3 is None else prim_edges3)


# 运行测试
test_mst_algorithms()
