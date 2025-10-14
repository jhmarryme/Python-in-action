from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 起始颜色和目标颜色一定要不同，不然会死循环！！！！
        if image[sr][sc] != color:
            old, image[sr][sc] = image[sr][sc], color
            for i, j in zip((sr, sr, sr - 1, sr + 1), (sc - 1, sc + 1, sc, sc)):
                if i >= 0 and i < len(image) and j >= 0 and j < len(image[0]) and image[i][j] == old:
                    self.floodFill(image, i, j, color)
        return image


print(Solution().floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0))
print(Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
