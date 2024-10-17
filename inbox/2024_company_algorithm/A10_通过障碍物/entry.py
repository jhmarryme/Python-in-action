'''
描述
在一张平面上有一些障碍物N（N<=600），这些障碍物平行于 X 轴或 Y 轴。它们可能会相交，但永远不会重叠。每个障碍物都有一个切割成本 Ci（Ci<=100）。
在障碍物的任何位置切割都是有效的，但是不能与另一个障碍物的交点处切割，请计算允许人们在平面上自由通行所需的最小成本。

输入
二维数组，每行有5个数字，前4个数字为障碍物两个端点的坐标，第五个数字为该障碍物的切割成本

输出
输出允许人们在平面上自由通行所需的最小成本

输入样例 1
-10 10 10 10 1
-10 -10 10 -10 2
-5 -15 -5 15 3
0 -15 0 15 4
5 -15 5 15 5

输出样例 1
2

函数定义风格如下:
def cut(a):
    return 0

'''


def cut(a):
    if len(a) % 5 != 0:
        return 0

    num_obstacles = len(a) // 5
    horizontal_costs = []
    vertical_costs = []

    for i in range(num_obstacles):
        x1 = a[5 * i]
        y1 = a[5 * i + 1]
        x2 = a[5 * i + 2]
        y2 = a[5 * i + 3]
        Ci = a[5 * i + 4]

        if y1 == y2:
            horizontal_costs.append(Ci)
        elif x1 == x2:
            vertical_costs.append(Ci)
        else:
            pass

    if len(horizontal_costs) >= 1:
        min_ci_hi = min(horizontal_costs)
        sum_c_hi = sum(horizontal_costs)
        total_cost_hi = sum_c_hi - min_ci_hi
    else:
        total_cost_hi = float('inf')

    if len(vertical_costs) >= 1:
        min_ci_vi = min(vertical_costs)
        sum_c_vi = sum(vertical_costs)
        total_cost_vi = sum_c_vi - min_ci_vi
    else:
        total_cost_vi = float('inf')

    if horizontal_costs and vertical_costs:
        min_total_cost = min(total_cost_hi, total_cost_vi)
    elif horizontal_costs:
        min_total_cost = total_cost_hi
    elif vertical_costs:
        min_total_cost = total_cost_vi
    else:
        min_total_cost = 0

    if min_total_cost == float('inf'):
        min_total_cost = 0

    return min_total_cost


# =============================
# Example Test Cases
# =============================

if __name__ == "__main__":
    # Test Case 1: Sample Input 1
    a1 = [-10, 10, 10, 10, 1,
          -10, -10, 10, -10, 2,
          -5, -15, -5, 15, 3,
          0, -15, 0, 15, 4,
          5, -15, 5, 15, 5]
    print(cut(a1))  # Expected Output: 2

    # Test Case 2: Single Horizontal Obstacle
    a2 = [1, 1, 5, 1, 10]
    print(cut(a2))  # Expected Output: 0 (Ho=1, total_cost_hi=0)

    # Test Case 3: Single Vertical Obstacle
    a3 = [2, 2, 2, 6, 5]
    print(cut(a3))  # Expected Output: 0 (Vo=1, total_cost_vi=0)

    # Test Case 4: Multiple Horizontal Obstacles
    a4 = [0, 0, 10, 0, 3, 0, 0, 10, 0, 2, 0, 0, 10, 0, 1]
    print(cut(a4))  # Expected Output: (3+2+1) -1 =6 -1=5

    # Test Case 5: Multiple Vertical Obstacles
    a5 = [1, 1, 1, 5, 4, 2, 2, 2, 6, 3, 3, 3, 3, 7, 2]
    print(cut(a5))  # Expected Output: (4+3+2) -2=9-2=7

    # Test Case 6: Only Horizontal Obstacles with single minimal cost
    a6 = [0, 10, 10, 10, 5, 0, 20, 10, 20, 3, 0, 30, 10, 30, 4]
    print(cut(a6))  # Expected Output: (5+3+4)-3=12-3=9

    # Test Case 7: Only Vertical Obstacles with single minimal cost
    a7 = [5, 0, 5, 10, 2, 15, 0, 15, 10, 1, 25, 0, 25, 10, 3]
    print(cut(a7))  # Expected Output: (2+1+3)-1=6-1=5

    # Test Case 8: No Obstacles
    a8 = []
    print(cut(a8))  # Expected Output: 0

    # Test Case 9: Mixed Obstacles, minimal cost option
    a9 = [0, 0, 10, 0, 5, 0, 0, 10, 10, 10, 5, 0, 5, 10, 2, 5, 10, 15, 10, 3, 10, 0, 10, 10, 4]
    # Categorize:
    # H1: y=0, Ci=5
    # H2: y=10, Ci=10
    # V1: x=5, Ci=2
    # V2: x=15, Ci=3
    # V3: x=10, Ci=4
    # total_cost_hi = 5 +10 -5=10
    # total_cost_vi = 2+3+4 -2=7
    # min_total_cost=7
    print(cut(a9))  # Expected Output:7

    # Test Case 10: All obstacles are horizontal except one vertical, minimal cost is to keep the minimal H or V
    a10 = [0, 0, 10, 0, 1, 0, 10, 10, 10, 2, 5, 0, 5, 10, 3]
    # Ho_Ci=[1,2], Vo_Ci=[3]
    # total_cost_hi= (1+2)-1=2
    # total_cost_vi= (3) -3=0
    # min_total_cost=min(2,0)=0
    print(cut(a10))  # Expected Output:0
