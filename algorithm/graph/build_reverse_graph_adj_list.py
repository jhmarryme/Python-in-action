def build_reverse_graph(graph):
    """构造有向图的逆图（邻接表格式）"""
    reverse = {node: [] for node in graph}

    for i in graph:
        for j in graph[i]:
            reverse[j].append(i)

    return reverse


graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: []
}

print(build_reverse_graph(graph))
