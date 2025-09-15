class Solution(object):
    def __init__(self):
        self.memo = {}

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        return self.dfs(triangle, 0, 0)

    def dfs(self, triangle, i, j):
        if i == len(triangle):
            return 0
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        self.memo[(i, j)] = min(self.dfs(triangle, i + 1, j), self.dfs(triangle, i + 1, j + 1)) + triangle[i][j]
        return self.memo[(i, j)]
