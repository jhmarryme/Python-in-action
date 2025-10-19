class Dsu:
    def __init__(self, size):
        self.pa = list(range(size))
        self.size = [1] * size

    def find(self, x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.pa[y] = x
        self.size[x] += self.size[y]
        return True


def kruskal(edges, size):
    sorted_edges = sorted(edges, key=lambda x: x[2])
    mst = []
    total_weight = 0
    dsu = Dsu(size)

    for u, v, weight in sorted_edges:
        if dsu.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            if len(mst) == size - 1:
                break
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
    # Kruskal测试
    kruskal_edges, kruskal_weight = kruskal(edges1, 5)
    print("Kruskal算法选中的边：", kruskal_edges)
    print("Kruskal算法总权重：", kruskal_weight)  # 预期：2+3+5+6=16

    # Prim测试（从顶点0开始）
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

    kruskal_edges2, kruskal_weight2 = kruskal(edges2, 4)
    print("Kruskal算法选中的边：", kruskal_edges2)
    print("Kruskal算法总权重：", kruskal_weight2)  # 预期：1+1+2=4

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

    kruskal_edges3, _ = kruskal(edges3, 5)
    print("Kruskal算法结果：", "无生成树" if kruskal_edges3 is None else kruskal_edges3)


test_mst_algorithms()
