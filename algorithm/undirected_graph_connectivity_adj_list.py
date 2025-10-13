from collections import deque


def is_connected_undirected_dfs(graph):
    if not graph:
        return True
    visited = set()
    start = next(iter(graph))

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return len(visited) == len(graph)


def is_connected_undirected_bfs(graph):
    if not graph:
        return True

    visited = set()
    start = next(iter(graph))
    queue = deque([start])
    while queue:
        node = queue.popleft()
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return len(visited) == len(graph)


if __name__ == "__main__":
    print("=== 图连通性测试用例 ===")

    # 测试用例1: 连通图 - 正方形
    graph1 = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2]
    }
    print(f"测试1 - 连通正方形图: DFS={is_connected_undirected_dfs(graph1)}, BFS={is_connected_undirected_bfs(graph1)}")

    # 测试用例2: 非连通图 - 两个分离的边
    graph2 = {
        0: [1],
        1: [0],
        2: [3],
        3: [2]
    }
    print(
        f"测试2 - 非连通图(两个边): DFS={is_connected_undirected_dfs(graph2)}, BFS={is_connected_undirected_bfs(graph2)}")

    # 测试用例3: 连通图 - 星形结构
    graph3 = {
        0: [1, 2, 3],
        1: [0],
        2: [0],
        3: [0]
    }
    print(f"测试3 - 连通星形图: DFS={is_connected_undirected_dfs(graph3)}, BFS={is_connected_undirected_bfs(graph3)}")

    # 测试用例4: 非连通图 - 三个分离的节点
    graph4 = {
        0: [],
        1: [],
        2: []
    }
    print(
        f"测试4 - 非连通图(三个孤立节点): DFS={is_connected_undirected_dfs(graph4)}, BFS={is_connected_undirected_bfs(graph4)}")

    # 测试用例5: 连通图 - 链式结构
    graph5 = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2]
    }
    print(f"测试5 - 连通链式图: DFS={is_connected_undirected_dfs(graph5)}, BFS={is_connected_undirected_bfs(graph5)}")

    # 测试用例6: 连通图 - 环状结构
    graph6 = {
        0: [1, 4],
        1: [0, 2],
        2: [1, 3],
        3: [2, 4],
        4: [3, 0]
    }
    print(f"测试6 - 连通环状图: DFS={is_connected_undirected_dfs(graph6)}, BFS={is_connected_undirected_bfs(graph6)}")

    # 测试用例7: 非连通图 - 一个连通分量和一个孤立节点
    graph7 = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1],
        3: []
    }
    print(
        f"测试7 - 非连通图(三角形+孤立节点): DFS={is_connected_undirected_dfs(graph7)}, BFS={is_connected_undirected_bfs(graph7)}")

    # 测试用例8: 空图
    graph8 = {}
    print(f"测试8 - 空图: DFS={is_connected_undirected_dfs(graph8)}, BFS={is_connected_undirected_bfs(graph8)}")

    # 测试用例9: 单节点图
    graph9 = {
        0: []
    }
    print(f"测试9 - 单节点图: DFS={is_connected_undirected_dfs(graph9)}, BFS={is_connected_undirected_bfs(graph9)}")

    # 测试用例10: 复杂非连通图
    graph10 = {
        0: [1],
        1: [0],
        2: [3, 4],
        3: [2, 4],
        4: [2, 3],
        5: []
    }
    print(
        f"测试10 - 复杂非连通图: DFS={is_connected_undirected_dfs(graph10)}, BFS={is_connected_undirected_bfs(graph10)}")
