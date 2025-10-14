def build_reverse_graph(graph):
    # 下面的写法有问题,赋值的问题类似于浅拷贝带来的问题
    # reverse = [[0] * len(graph)] * len(graph)
    reverse = [[0] * len(graph) for _ in range(len(graph))]

    for u in range(len(graph)):
        for v in range(len(graph[u])):
            if graph[u][v] == 1:
                reverse[v][u] = 1
    return reverse


graph = [
    [0, 1, 0],  # 0→1
    [0, 0, 1],  # 1→2
    [1, 0, 0]  # 2→0（闭环保证互达）
]

print(build_reverse_graph(graph))
