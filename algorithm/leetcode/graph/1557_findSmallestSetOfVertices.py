from typing import List


class Solution:
    """
    1557. 可以到达所有点的最少点数目
    """

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # 用数组会超时
        degree = set(y for x, y in edges)
        return [i for i in range(n) if i not in degree]


n = 5
edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
print(Solution().findSmallestSetOfVertices(n, edges))
