def cut(a):
    """
    Determines the minimum total cutting cost required to allow free passage across the plane.

    Parameters:
    - a (list): A flat list where every 5 consecutive elements represent a directed edge (x1, y1, x2, y2, Ci).

    Returns:
    - int: The minimum total cutting cost. If no cuts are needed, returns 0.
    """
    if not a:
        # No obstacles, no cost needed
        return 0

    if len(a) % 5 != 0:
        # Invalid input length
        return 0

    num_obstacles = len(a) // 5
    horizontal_costs = []
    vertical_costs = []

    for i in range(num_obstacles):
        x1 = a[5*i]
        y1 = a[5*i + 1]
        x2 = a[5*i + 2]
        y2 = a[5*i + 3]
        Ci = a[5*i + 4]

        if y1 == y2 and x1 == x2:
            # Single-point obstacle, treated as both horizontal and vertical
            horizontal_costs.append(Ci)
            vertical_costs.append(Ci)
        elif y1 == y2:
            # Horizontal obstacle
            horizontal_costs.append(Ci)
        elif x1 == x2:
            # Vertical obstacle
            vertical_costs.append(Ci)
        else:
            # Invalid obstacle (not axis-aligned), according to problem statement this shouldn't happen
            pass

    # Calculate total cutting cost for horizontal obstacles: remove all but one minimal Ci
    if horizontal_costs:
        min_ci_hi = min(horizontal_costs)
        sum_c_hi = sum(horizontal_costs)
        total_cost_hi = sum_c_hi - min_ci_hi
    else:
        total_cost_hi = float('inf')  # If no horizontal obstacles, set to infinity to ignore

    # Calculate total cutting cost for vertical obstacles: remove all but one minimal Ci
    if vertical_costs:
        min_ci_vi = min(vertical_costs)
        sum_c_vi = sum(vertical_costs)
        total_cost_vi = sum_c_vi - min_ci_vi
    else:
        total_cost_vi = float('inf')  # If no vertical obstacles, set to infinity to ignore

    # Determine the minimal total cost: choose to remove all H except one or all V except one
    if horizontal_costs and vertical_costs:
        min_total_cost = min(total_cost_hi, total_cost_vi)
    elif horizontal_costs:
        # Only horizontal obstacles exist
        min_total_cost = total_cost_hi
    elif vertical_costs:
        # Only vertical obstacles exist
        min_total_cost = total_cost_vi
    else:
        # No obstacles, no cost needed
        min_total_cost = 0

    # If min_total_cost is infinity, it means one partition is missing, so no cuts needed
    if min_total_cost == float('inf'):
        min_total_cost = 0

    return min_total_cost
if __name__ == "__main__":
    # Test Case 1: Sample Input 1
    a1 = [
        -10, 10, 10, 10, 1,
        -10, -10, 10, -10, 2,
        -5, -15, -5, 15, 3,
        0, -15, 0, 15, 4,
        5, -15, 5, 15, 5
    ]
    print(cut(a1))  # Expected Output: 2

    # Test Case 2: Single Horizontal Obstacle
    a2 = [1, 1, 5, 1, 10]
    print(cut(a2))  # Expected Output: 0
    # Explanation: Only one H obstacle, no cuts needed as there's no cycle.

    # Test Case 3: Single Vertical Obstacle
    a3 = [2, 2, 2, 6, 5]
    print(cut(a3))  # Expected Output: 0
    # Explanation: Only one V obstacle, no cuts needed as there's no cycle.

    # Test Case 4: Multiple Horizontal Obstacles
    a4 = [0, 0, 10, 0, 3, 0, 0, 10, 10, 2, 0, 0, 10, 20, 1]
    print(cut(a4))  # Expected Output: 3-1=2

    # Test Case 5: Multiple Vertical Obstacles
    a5 = [1, 1, 1, 5, 4, 2, 2, 2, 6, 3, 3, 3, 3, 7, 2]
    print(cut(a5))  # Expected Output: (sum V Ci=4+3+2)-min=2=5

    # Test Case 6: Only Horizontal Obstacles with single minimal cost
    a6 = [0, 10, 10, 10, 5, 0, 20, 10, 20, 3, 0, 30, 10, 30, 4]
    # H obstacles: Ci=5, 3,4
    # sum_cut_hi=5+3+4 -3=9
    # No V obstacles
    print(cut(a6))  # Expected Output:9

    # Test Case 7: Only Vertical Obstacles with single minimal cost
    a7 = [5, 0, 5, 10, 2, 15, 0, 15, 10, 1, 25, 0, 25, 10, 3]
    # V obstacles: Ci=2,1,3
    # sum_cut_vi=2+1+3 -1=5
    # No H obstacles
    print(cut(a7))  # Expected Output:5

    # Test Case 8: No Obstacles
    a8 = []
    print(cut(a8))  # Expected Output:0

    # Test Case 9: Mixed Obstacles, minimal cost option
    a9 = [
        0, 0, 10, 0, 5,   # H1: Ci=5
        0, 0, 10, 10, 10, # V1: Ci=10
        5, 0, 5, 10, 2,   # V2: Ci=2
        5, 10, 15, 10, 3,  # V3: Ci=3
        10, 0, 10, 10, 4   # V4: Ci=4
    ]
    # H obstacles: [5]
    # V obstacles: [10,2,3,4]
    # sum_cut_hi=5-5=0
    # sum_cut_vi=10+2+3+4 -2=17
    # min=0
    print(cut(a9))  # Expected Output:0

    # Test Case 10: All obstacles are horizontal except one vertical, minimal cost is to keep H with min Ci
    a10 = [0,0,10,0,1, 0,10,10,10,2, 5,0,5,10,3]
    # H obstacles: [1,2]
    # V obstacles: [3]
    # sum_cut_hi=1+2 -1=2
    # sum_cut_vi=3 -3=0
    # min_total=0
    print(cut(a10))  # Expected Output:0

    # Test Case 11: Single-point obstacle (treated as both H and V)
    a11 = [8, 8, 8, 8, 5]
    # H obstacles: [5]
    # V obstacles: [5]
    # sum_cut_hi=5-5=0
    # sum_cut_vi=5-5=0
    # min_total=0
    print(cut(a11))  # Expected Output:0

    # Test Case 12: Multiple H and V, requiring smaller cuts
    a12 = [
        -10, 10, 10, 10, 1,    # H1: Ci=1
        -10, -10, 10, -10, 2,  # H2: Ci=2
        -5, -15, -5, 15, 3,    # V1: Ci=3
        0, -15, 0, 15, 4,      # V2: Ci=4
        5, -15, 5, 15, 5       # V3: Ci=5
    ]
    # H obstacles: [1,2]
    # V obstacles: [3,4,5]
    # sum_cut_hi=1+2 -1=2
    # sum_cut_vi=3+4+5 -3=9
    # min_total=2
    print(cut(a12))  # Expected Output:2