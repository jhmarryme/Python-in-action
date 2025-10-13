def is_strongly_connected_directed(graph):
    def build_reverse_graph(graph):
        # reverse = [[0] * len(graph)] * len(graph)
        reverse = [[0] * len(graph) for _ in range(len(graph))]

        for u in range(len(graph)):
            for v in range(len(graph[u])):
                if graph[u][v] == 1:
                    reverse[v][u] = 1
        return reverse

    def dfs_connectivity(matrix):
        visited = [False] * len(matrix)

        def dfs(i):
            visited[i] = True
            for j in range(len(matrix)):
                if not visited[j] and matrix[i][j] == 1:
                    dfs(j)

        dfs(0)
        return all(visited)

    if not dfs_connectivity(graph):
        return False
    return dfs_connectivity(build_reverse_graph(graph))


# 有向图测试1：强连通图（3个顶点形成闭环：0→1，1→2，2→0）
strongly_connected_dir_matrix = [
    [0, 1, 0],  # 0→1
    [0, 0, 1],  # 1→2
    [1, 0, 0]  # 2→0（闭环保证互达）
]
print("\n=== 有向图测试1（强连通图） ===")
print(f"强连通判断结果：{is_strongly_connected_directed(strongly_connected_dir_matrix)}")  # True

# 有向图测试2：非强连通图（0→1→2，但2无法到0）
weakly_connected_dir_matrix = [
    [0, 1, 0],  # 0→1
    [0, 0, 1],  # 1→2
    [0, 0, 0]  # 2无出边，无法到0/1
]
print("\n=== 有向图测试2（非强连通图） ===")
print(f"强连通判断结果：{is_strongly_connected_directed(weakly_connected_dir_matrix)}")  # False
