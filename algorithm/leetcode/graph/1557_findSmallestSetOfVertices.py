import collections
from collections import deque
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)

        def bfs(start):
            component = list()
            visited = set()
            visited.add(start)
            queue = deque([start])
            while queue:
                node = queue.popleft()
                component.append(node)
                for neighbor in adj_list[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            components.append(component)

        components = list()
        for k in range(n):
            if len(adj_list[k]) > 0:
                bfs(k)
        print(components)


n = 6
edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
Solution().findSmallestSetOfVertices(n, edges)
