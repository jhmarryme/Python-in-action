class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m, n = len(heights), len(heights[0])
        left, right, ans = 0, max([num for rows in heights for num in rows]), 0
        while left <= right:
            mid = (left + right) // 2
            seen = set()

            def dfs(i, j):
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n and (x, y) not in seen and abs(heights[i][j] - heights[x][y]) <= mid:
                        seen.add((x, y))
                        dfs(x, y)

            seen.add((0, 0))
            dfs(0, 0)
            if (m - 1, n - 1) in seen:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
print(Solution().minimumEffortPath(heights))
