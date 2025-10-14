from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        count = 0
        n = len(isConnected)
        visited = [False] * n

        def dfs(i):
            for j in range(n):
                if not visited[j] and isConnected[i][j] == 1:
                    visited[i] = True
                    dfs(j)

        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        return count


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(Solution().findCircleNum(isConnected))
