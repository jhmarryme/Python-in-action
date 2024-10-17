def group(n, m, a):
    from sys import setrecursionlimit, stdin
    from collections import defaultdict, deque

    setrecursionlimit(10**6)

    # 构建图
    graph = defaultdict(list)
    for si, ti in a:
        graph[si - 1].append(ti - 1)

    # Tarjan's SCC Algorithm
    index = 0
    indexes = [-1] * n
    lowlink = [-1] * n
    stack = []
    on_stack = [False] * n
    scc_count = 0

    def tarjan(v):
        nonlocal index, scc_count
        indexes[v] = lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if indexes[w] == -1:
                tarjan(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indexes[w])

        if lowlink[v] == indexes[v]:
            while True:
                w = stack.pop()
                on_stack[w] = False
                if w == v:
                    break
            scc_count += 1

    for v in range(n):
        if indexes[v] == -1:
            tarjan(v)

    return scc_count

# 示例输入
n = 4
m = 4
a = [
    [1, 2],
    [1, 3],
    [2, 4],
    [3, 4]
]

result = group(n, m, a)
print(result)  # 输出: 3
