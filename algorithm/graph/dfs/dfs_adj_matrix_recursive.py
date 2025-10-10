def dfs_adj_matrix_recursive(matrix, start, visited=None):
    if visited is None:
        visited = list()
    print(start)
    visited.append(start)
    n = len(matrix)
    for i in range(n):
        if matrix[start][i] == 1 and i not in visited:
            dfs_adj_matrix_recursive(matrix, i, visited)
    return visited

# 邻接矩阵
adj_matrix = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0]
]

print("\n\n=== 邻接矩阵测试 ===")
print("DFS递归遍历:")
res = dfs_adj_matrix_recursive(adj_matrix, 0)  # 预期: 0 1 3 4 5 2
print(res)

