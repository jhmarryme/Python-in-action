import collections
from collections import deque
from typing import List

"""
1319. 连通网络的操作次数
"""


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        adj_list = collections.defaultdict(list)
        # 将connections转换为邻接表
        for x, y in connections:
            adj_list[x].append(y)
            adj_list[y].append(x)
        # 求连通分量数
        visited = set()

        def bfs(start):
            queue = deque([start])
            visited.add(start)
            while queue:
                i = queue.popleft()
                for neighbor in adj_list[i]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        count = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                count += 1
        return count - 1


n = 5
connections = [[0, 1], [0, 2], [3, 4], [2, 3]]

print(Solution().makeConnected(n, connections))
