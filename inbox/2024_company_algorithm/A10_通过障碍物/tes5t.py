def do_intersect(p1, q1, p2, q2):
    def on_segment(p, q, r):
        return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
                q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0: return 0  # collinear
        return 1 if val > 0 else 2  # clock or counterclock wise

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # Special Cases
    if o1 == 0 and on_segment(p1, p2, q1): return True
    if o2 == 0 and on_segment(p1, q2, q1): return True
    if o3 == 0 and on_segment(p2, p1, q2): return True
    if o4 == 0 and on_segment(p2, q1, q2): return True

    return False

def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find_parent(parent, x)
    yroot = find_parent(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(edges, n):
    result = []
    i, e = 0, 0
    edges.sort(key=lambda item: item[2])
    parent = [i for i in range(n)]
    rank = [0] * n

    while e < n - 1:
        u, v, w = edges[i]
        i += 1
        x = find_parent(parent, u)
        y = find_parent(parent, v)

        if x != y:
            e += 1
            result.append([u, v, w])
            union(parent, rank, x, y)

    total_cost = sum(edge[2] for edge in result)
    return total_cost

def cut(a):
    if len(a) % 5 != 0:
        return 0

    num_obstacles = len(a) // 5
    obstacles = []

    for i in range(num_obstacles):
        x1, y1, x2, y2, Ci = a[5 * i:5 * i + 5]
        obstacles.append(((x1, y1), (x2, y2), Ci))

    edges = []

    # 创建所有可能的边
    for i in range(num_obstacles):
        for j in range(i + 1, num_obstacles):
            p1, q1, cost1 = obstacles[i]
            p2, q2, cost2 = obstacles[j]

            # 如果两个障碍物相交，则跳过这条边
            if do_intersect(p1, q1, p2, q2):
                continue

            # 添加边
            edges.append((i, j, cost1 + cost2))

    # 计算最小生成树的总成本
    return kruskal(edges, num_obstacles)

# 示例测试
a = [
    -10, 10, 10, 10, 1,
    -10, -10, 10, -10, 2,
    -5, -15, -5, 15, 3,
    0, -15, 0, 15, 4,
    5, -15, 5, 15, 5
]
print(cut(a))  # 应输出 2