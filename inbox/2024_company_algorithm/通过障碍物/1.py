from collections import defaultdict, deque
# 4分
# 创建一个图类来处理最大流问题
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # 节点数量
        self.graph = defaultdict(list)  # 使用字典的邻接表来存储图
        self.capacity = {}  # 容量矩阵

    # 添加边
    def add_edge(self, u, v, w):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[(u, v)] = w
        self.capacity[(v, u)] = 0  # 反向边容量为0

    # 使用BFS寻找增广路径
    def bfs(self, source, sink, parent):
        visited = [False] * self.V
        queue = deque([source])
        visited[source] = True
        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if not visited[v] and self.capacity[(u, v)] > 0:  # 只考虑残余容量大于0的边
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    # 实现Edmonds-Karp算法（基于BFS的Ford-Fulkerson方法）
    def edmonds_karp(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0  # 最大流初始化为0

        # 不断寻找增广路径
        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.capacity[(parent[s], s)])
                s = parent[s]

            # 更新残余网络中的容量
            v = sink
            while v != source:
                u = parent[v]
                self.capacity[(u, v)] -= path_flow
                self.capacity[(v, u)] += path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow

def cut(obstacles):
    points = set()  # 存储所有节点
    index_map = {}  # 映射点坐标到节点索引
    edges = []

    # 收集所有的节点并建立点索引
    idx = 0
    for x1, y1, x2, y2, cost in obstacles:
        points.add((x1, y1))
        points.add((x2, y2))
        if (x1, y1) not in index_map:
            index_map[(x1, y1)] = idx
            idx += 1
        if (x2, y2) not in index_map:
            index_map[(x2, y2)] = idx
            idx += 1
        edges.append((index_map[(x1, y1)], index_map[(x2, y2)], cost))

    V = len(points)
    source = 0  # 假设第一个节点为源
    sink = V - 1  # 假设最后一个节点为汇

    graph = Graph(V)

    # 构建图
    for u, v, cost in edges:
        graph.add_edge(u, v, cost)

    # 求解最小割
    min_cut_cost = graph.edmonds_karp(source, sink)
    return min_cut_cost

# 测试输入
obstacles = [
    [-10, 10, 10, 10, 1],
    [-10, -10, 10, -10, 2],
    [-5, -15, -5, 15, 3],
    [0, -15, 0, 15, 4],
    [5, -15, 5, 15, 5]
]

# 调用cut函数
print(cut(obstacles))  # 输出: 2
