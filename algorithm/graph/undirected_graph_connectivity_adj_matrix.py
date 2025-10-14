from collections import deque


def is_connected_matrix_dfs(matrix):
    if not matrix:
        return True
    visited = [False] * len(matrix)

    def dfs(i):
        visited[i] = True
        for j in range(len(matrix)):
            if not visited[j] and matrix[i][j] == 1:
                dfs(j)

    dfs(0)
    return all(visited)


def is_connected_matrix_bfs(matrix):
    if not matrix:
        return True

    visited = [False] * len(matrix)
    queue = deque([0])
    while queue:
        i = queue.popleft()
        visited[i] = True
        for j in range(len(matrix)):
            if not visited[j] and matrix[i][j] == 1:
                queue.append(j)
    return all(visited)


if __name__ == "__main__":
    print("=== 邻接矩阵图连通性测试用例 ===")

    # 测试用例1: 连通图 - 正方形
    matrix1 = [
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [0, 1, 1, 0]
    ]
    print(f"测试1 - 连通正方形图: DFS={is_connected_matrix_dfs(matrix1)}, BFS={is_connected_matrix_bfs(matrix1)}")

    # 测试用例2: 非连通图 - 两个分离的边
    matrix2 = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ]
    print(f"测试2 - 非连通图(两个边): DFS={is_connected_matrix_dfs(matrix2)}, BFS={is_connected_matrix_bfs(matrix2)}")

    # 测试用例3: 连通图 - 星形结构
    matrix3 = [
        [0, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0]
    ]
    print(f"测试3 - 连通星形图: DFS={is_connected_matrix_dfs(matrix3)}, BFS={is_connected_matrix_bfs(matrix3)}")

    # 测试用例4: 非连通图 - 三个分离的节点
    matrix4 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print(
        f"测试4 - 非连通图(三个孤立节点): DFS={is_connected_matrix_dfs(matrix4)}, BFS={is_connected_matrix_bfs(matrix4)}")

    # 测试用例5: 连通图 - 链式结构
    matrix5 = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0]
    ]
    print(f"测试5 - 连通链式图: DFS={is_connected_matrix_dfs(matrix5)}, BFS={is_connected_matrix_bfs(matrix5)}")

    # 测试用例6: 连通图 - 环状结构
    matrix6 = [
        [0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0]
    ]
    print(f"测试6 - 连通环状图: DFS={is_connected_matrix_dfs(matrix6)}, BFS={is_connected_matrix_bfs(matrix6)}")

    # 测试用例7: 非连通图 - 一个连通分量和一个孤立节点
    matrix7 = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    print(
        f"测试7 - 非连通图(三角形+孤立节点): DFS={is_connected_matrix_dfs(matrix7)}, BFS={is_connected_matrix_bfs(matrix7)}")

    # 测试用例8: 空图
    matrix8 = []
    print(f"测试8 - 空图: DFS={is_connected_matrix_dfs(matrix8)}, BFS={is_connected_matrix_bfs(matrix8)}")

    # 测试用例9: 单节点图
    matrix9 = [
        [0]
    ]
    print(f"测试9 - 单节点图: DFS={is_connected_matrix_dfs(matrix9)}, BFS={is_connected_matrix_bfs(matrix9)}")

    # 测试用例10: 复杂非连通图
    matrix10 = [
        [0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(f"测试10 - 复杂非连通图: DFS={is_connected_matrix_dfs(matrix10)}, BFS={is_connected_matrix_bfs(matrix10)}")
