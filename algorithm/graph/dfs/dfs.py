def dfs(matrix, node, visited, traversal_order):
    """
    递归执行DFS遍历单个连通分量，并记录遍历顺序
    参数:
        matrix: 邻接矩阵，表示图的连接关系
        node: 当前遍历的节点
        visited: 已访问节点的集合，用于避免重复访问
        traversal_order: 记录遍历顺序的列表
    """
    # 标记当前节点为已访问
    visited.add(node)
    # 将当前节点添加到遍历顺序列表中
    traversal_order.append(node)
    # 打印当前节点（可选）
    print(node, end=' ')

    # 遍历当前节点的所有可能邻居
    for neighbor in range(len(matrix)):
        # 若存在边连接且邻居未被访问，则递归访问该邻居
        if matrix[node][neighbor] == 1 and neighbor not in visited:
            dfs(matrix, neighbor, visited, traversal_order)

def dfs_traverse_all(matrix):
    """
    自动遍历图中所有连通分量，返回按遍历顺序排列的节点数组
    参数:
        matrix: 邻接矩阵
    返回:
        按DFS遍历顺序排列的节点列表
    """
    # 边界检查：空矩阵或非方阵直接返回空列表
    if not matrix or len(matrix) != len(matrix[0]):
        return []

    visited = set()
    all_nodes = set(range(len(matrix)))
    # 用于记录完整遍历顺序的列表
    traversal_order = []

    print("DFS遍历结果：")
    # 处理所有连通分量
    while visited != all_nodes:
        # 找到下一个未访问的节点作为起始点
        start_node = (all_nodes - visited).pop()
        # 从起始点开始DFS，同时记录遍历顺序
        dfs(matrix, start_node, visited, traversal_order)

    return traversal_order

# 测试1：连通图
connected_matrix = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0]
]

print("连通图测试：")
connected_result = dfs_traverse_all(connected_matrix)
print("\n遍历顺序数组：", connected_result)
print("\n")

# 测试2：非连通图
disconnected_matrix = [
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

print("非连通图测试：")
disconnected_result = dfs_traverse_all(disconnected_matrix)
print("\n遍历顺序数组：", disconnected_result)
