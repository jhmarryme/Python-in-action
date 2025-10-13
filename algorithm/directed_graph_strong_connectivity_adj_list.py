def is_strongly_connected_directed(graph):
    def build_reverse_graph(graph):
        reverse = {node: [] for node in graph}
        for u in graph:
            for v in graph[u]:
                reverse[v].append(u)
        return reverse

    def dfs_connectivity(graph):
        visited = set()
        start = next(iter(graph))

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start)
        return len(visited) == len(graph)

    if not dfs_connectivity(graph):
        return False

    return dfs_connectivity(build_reverse_graph(graph))


g1 = {0: [1], 1: [2], 2: [0]}  # 强连通
g2 = {0: [1], 1: [2], 2: []}  # 非强连通

print(is_strongly_connected_directed(g1))  # True
print(is_strongly_connected_directed(g2))  # False
