from typing import List

'''
思路来源于:
https://leetcode.cn/problems/surrounded-regions/solutions/2821578/xin-shou-xiang-wu-pen-cong-t200dao-yu-we-8paj/
'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O':
                return
            board[i][j] = 'E'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # 对边界做dfs, 边界O为起点 相邻处理为E
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols - 1)
        for j in range(cols - 2):
            dfs(0, j + 1)
            dfs(rows - 1, j + 1)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    # 处理 O 为 X, 剩下的一定被X包围, 不用再做dfs了
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    # 处理 E 为 O
                    board[i][j] = 'O'
        print(board)


board = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
Solution().solve(board)
