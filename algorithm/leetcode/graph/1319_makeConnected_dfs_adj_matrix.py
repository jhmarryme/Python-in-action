from typing import List

"""
1319. 连通网络的操作次数
邻接矩阵会内存超限
"""


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for x, y in connections:
            matrix[x][y] = 1
            matrix[y][x] = 1

        visited = [False] * n

        def dfs(i):
            visited[i] = True
            for j in range(n):
                if not visited[j] and matrix[i][j] == 1:
                    dfs(j)

        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count - 1


n = 6
connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]

print(Solution().makeConnected(n, connections))
