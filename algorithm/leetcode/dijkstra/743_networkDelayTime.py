import collections
import sys
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        visited = [False] * n
        dist = [sys.maxsize] * n
        start = k - 1
        for u, v, w  in times:
            graph[u - 1].append([v - 1, w])
        print(graph)
        dist[start] = 0
        for _ in range(n):
            u = - 1
            min_dist = sys.maxsize
            for i in range(n):
                if not visited[i] and dist[i] < min_dist:
                    u = i
                    min_dist = dist[i]
            if u == - 1:
                break
            visited[u] = True
            for x, y in graph[u]:
                if not visited[x] and dist[u] + y < dist[x]:
                    dist[x] = dist[u] + y

        res = max(dist)
        return res if res != sys.maxsize else -1


times = [[1,2,1]]
n = 2
k = 2
print(Solution().networkDelayTime(times, n, k))
