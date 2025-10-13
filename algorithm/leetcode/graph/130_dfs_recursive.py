from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])

        def dfs(i, j, target):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O':
                return
            board[i][j] = target
            dfs(i + 1, j, target)
            dfs(i - 1, j, target)
            dfs(i, j + 1, target)
            dfs(i, j - 1, target)

        # 对边界做dfs, 边界O为起点 相邻处理为E
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    if board[i][j] == 'O':
                        dfs(i, j, 'E')
        # 进行dfs 处理 O 为 X
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    dfs(i, j, 'X')
        # 将E还原为O

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'E':
                    board[i][j] = 'O'

        print(board)


board = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
Solution().solve(board)
