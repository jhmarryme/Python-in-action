from collections import deque
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        left, right, res = 0, max([num for row in heights for num in row]), 0
        while left <= right:
            mid = (left + right) // 2
            # 这里用数组会超时
            # 列表的in操作是线性查找（逐个遍历元素对比），时间复杂度为 O(k)（k 是列表长度）。
            # 集合的in操作是哈希查找（通过哈希值直接定位），平均时间复杂度为 O(1)（几乎不随集合大小变化）。
            seen = {(0, 0)}
            queue = deque([(0, 0)])
            while queue:
                x, y = queue.popleft()
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and abs(
                            heights[nx][ny] - heights[x][y]) <= mid:
                        queue.append((nx, ny))
                        seen.add((nx, ny))
                        if nx == m - 1 and ny == n - 1:
                            break
            if (m - 1, n - 1) in seen:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res


heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
print(Solution().minimumEffortPath(heights))
