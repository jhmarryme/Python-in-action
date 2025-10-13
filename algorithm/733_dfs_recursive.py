from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 起始颜色和目标颜色一定要不同，不然会死循环！！！！
        if image[sr][sc] == color:
            return image
        rows = len(image)
        cols = len(image[0])
        init_color = image[sr][sc]

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            if image[i][j] != init_color:
                return
            image[i][j] = color
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        dfs(sr, sc)
        return image


print(Solution().floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0))
print(Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
