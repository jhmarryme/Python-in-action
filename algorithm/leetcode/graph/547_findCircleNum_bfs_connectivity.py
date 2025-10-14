from collections import deque
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

        def bfs(start):
            queue = deque([start])
            while queue:
                i = queue.popleft()
                visited[i] = True
                for j in range(n):
                    if not visited[j] and isConnected[i][j] == 1:
                        queue.append(j)

        for i in range(n):
            if not visited[i]:
                count += 1
                bfs(i)
        return count


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(Solution().findCircleNum(isConnected))
