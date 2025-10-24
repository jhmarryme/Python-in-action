from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        edges = []
        dsu = Dsu(m * n)
        for i in range(m):
            for j in range(n):
                k = i * n + j
                if i < m - 1:
                    edges.append([k, k + n, abs(heights[i][j] - heights[i + 1][j])])
                if j < n - 1:
                    edges.append([k, k + 1, abs(heights[i][j] - heights[i][j + 1])])
        edges.sort(key=lambda x: x[2])
        for u, v, w in edges:
            dsu.union(u, v)
            if dsu.is_connected(0, m * n - 1):
                return w
        return 0


class Dsu:
    def __init__(self, n):
        self.pa = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.pa[y] = x
        self.size[x] += self.size[y]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


heights = [[1, 10, 6, 7, 9, 10, 4, 9]]
print(Solution().minimumEffortPath(heights))
