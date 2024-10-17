'''
连续区域
描述

给定一个n*m的二维位图，位图中的值为0或者1。请计算这个二维位图中连通的1的区域的个数。

所谓的连通是指为位图中为1值的位置，在其周围（上、下、左、右、左上、左下、右上、右下）有1值。

如下列位图中有2个连通的区域。

1 1 0 0 1
1 0 0 1 0
1 1 0 1 1
0 1 0 0 1
下图中就有3个连通区域

1 0 0 0 0 0 0 0 0 1 1 0
0 1 1 1 0 0 0 0 0 1 1 1
0 0 0 0 1 1 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0 1 0 0
0 0 1 0 0 0 0 0 0 1 0 0
0 1 0 1 0 0 0 0 0 1 1 0
1 0 1 0 1 0 0 0 0 0 1 0
0 1 0 1 0 0 0 0 0 0 1 0
0 0 1 0 0 0 0 0 0 0 1 0
现在给定个n*m的位图，请你编写一段代码，计算出此位图中连通区域的个数k.

输入
一个n*m的二维数组位图，1<=n,m<=1000

输出
位图中连通区域的个数k

输入样例 1

bool map[][] = [
[ 1 0 0 0 0 0 0 0 0 1 1 0 ],
[ 0 1 1 1 0 0 0 0 0 1 1 1 ],
[ 0 0 0 0 1 1 0 0 0 1 1 0 ],
[ 0 0 0 0 0 0 0 0 0 1 1 0 ],
[ 0 0 0 0 0 0 0 0 0 1 0 0 ],
[ 0 0 1 0 0 0 0 0 0 1 0 0 ],
[ 0 1 0 1 0 0 0 0 0 1 1 0 ],
[ 1 0 1 0 1 0 0 0 0 0 1 0 ],
[ 0 1 0 1 0 0 0 0 0 0 1 0 ],
[ 0 0 1 0 0 0 0 0 0 0 1 0 ]
]
输出样例 1

3

函数定义风格如下:
def find_successive_area_number(bits: [[bool]], n: int, m: int) -> int:
return 0
'''

# 答案正确

from collections import deque
from typing import List

def find_successive_area_number(bits: List[List[bool]], n: int, m: int) -> int:
    """
    Counts the number of connected regions of 1's in a 2D bitmap.

    Parameters:
    - bits (List[List[bool]]): 2D list representing the bitmap, where each sublist represents a row.
    - n (int): Number of rows in the bitmap.
    - m (int): Number of columns in the bitmap.

    Returns:
    - int: Number of connected regions of 1's.
    """
    if n == 0 or m == 0:
        return 0

    # Directions: 8 possible moves (including diagonals)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    region_count = 0

    for i in range(n):
        for j in range(m):
            if bits[i][j]:
                region_count += 1
                # Start BFS from this cell
                queue = deque()
                queue.append((i, j))
                bits[i][j] = False  # Mark as visited

                while queue:
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        new_x, new_y = x + dx, y + dy
                        # Check boundaries
                        if 0 <= new_x < n and 0 <= new_y < m and bits[new_x][new_y]:
                            queue.append((new_x, new_y))
                            bits[new_x][new_y] = False  # Mark as visited

    return region_count

# =========================
# Example Test Cases
# =========================
if __name__ == "__main__":
    # Helper function to convert list of lists with integers to booleans
    def convert_to_bool(grid_int: List[List[int]]) -> List[List[bool]]:
        return [[bool(cell) for cell in row] for row in grid_int]

    # Sample Input 1
    grid1_int = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    ]
    grid1 = convert_to_bool(grid1_int)
    n1, m1 = 10, 12
    print(find_successive_area_number(grid1, n1, m1))  # Expected Output: 3

    # Additional Test Case 2: Two connected regions
    grid2_int = [
        [1, 1, 0, 0, 1],
        [1, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 1, 0, 0, 1]
    ]
    grid2 = convert_to_bool(grid2_int)
    n2, m2 = 4, 5
    print(find_successive_area_number(grid2, n2, m2))  # Expected Output: 2

    # Additional Test Case 3: One connected region
    grid3_int = [
        [1, 1],
        [1, 1]
    ]
    grid3 = convert_to_bool(grid3_int)
    n3, m3 = 2, 2
    print(find_successive_area_number(grid3, n3, m3))  # Expected Output: 1

    # Additional Test Case 4: No connected regions
    grid4_int = [
        [0, 0],
        [0, 0]
    ]
    grid4 = convert_to_bool(grid4_int)
    n4, m4 = 2, 2
    print(find_successive_area_number(grid4, n4, m4))  # Expected Output: 0

    # Additional Test Case 5: Mixed regions
    grid5_int = [
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1]
    ]
    grid5 = convert_to_bool(grid5_int)
    n5, m5 = 4, 4
    print(find_successive_area_number(grid5, n5, m5))  # Expected Output: 8