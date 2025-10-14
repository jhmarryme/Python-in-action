import collections
from typing import List


"""
1319. 连通网络的操作次数
"""
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        adj_list = collections.defaultdict(list)
        for x, y in connections:
            adj_list[x].append(y)
            adj_list[y].append(x)

        visited = [False] * n

        def dfs(i):
            visited[i] = True
            for j in adj_list[i]:
                if not visited[j]:
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
