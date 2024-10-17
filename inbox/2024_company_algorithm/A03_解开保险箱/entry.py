'''
解开保险箱
描述

小美有一个保险箱，某天她想打开罐子看看里面存了多少钱。
保险箱的锁是由N个相同的圆盘组成，每个圆盘分为10,000,000个相同的段，按顺时针方向从1到10,000,000编号。开始时，所有圆盘上的相同编号的段彼此上下对齐。圆盘叠放在一起，使得这些段相互重叠，每个圆盘正好缺少一个段，称为“孔”。
为了解锁保险箱，所有的孔必须上下对齐。小美转动一个圆盘任意方向（顺时针或逆时针）一格需要花费一秒钟。

请编写一个程序，帮助小美用最短的时间来打开保险箱。

输入
输入为数组，第一个元素表示圆盘的数量 (N ≥ 2)。后面第(i+1) 个元素为一个整数，表示第i（i >= 1）个圆盘上孔的初始位置。

输出
输出的第一行为小美解锁保险箱所需的最短时间（单位：秒）。


输入样例 1
[4,9999999,7,16,9999995]
输出样例 1
29

函数定义风格如下:
def minTime(inArr):
    return 1

'''


# 答案正确
def minTime(inArr):
    N = inArr[0]
    positions = inArr[1:N + 1]
    LOCK_SIZE = 10_000_000  # Number of segments per disk

    # To avoid redundant target positions, consider unique positions
    unique_targets = set(positions)
    min_total_time = float('inf')

    for t in unique_targets:
        total_time = 0
        for p in positions:
            diff = abs(t - p)
            rotation_steps = min(diff, LOCK_SIZE - diff)
            total_time += rotation_steps
        if total_time < min_total_time:
            min_total_time = total_time

    return min_total_time


# =========================
# Example Test Cases
# =========================
if __name__ == "__main__":
    # Test Case 1
    inArr1 = [4, 9999999, 7, 16, 9999995]
    print(minTime(inArr1))  # Expected Output: 29

    # Test Case 2: All holes already aligned
    inArr2 = [3, 5000000, 5000000, 5000000]
    print(minTime(inArr2))  # Expected Output: 0

    # Test Case 3: Minimal rotation
    inArr3 = [2, 1, 10000000]
    # Aligning to 1: min(0,0) + min(9999999,1) =0 +1=1
    # Aligning to 10000000: min(0,0) + min(1,9999999)=0 +1=1
    print(minTime(inArr3))  # Expected Output: 1

    # Test Case 4: Diverse positions
    inArr4 = [5, 1, 5000000, 10000000, 2500000, 7500000]
    # Possible targets: 1, 5000000, 10000000, 2500000, 7500000
    # Calculate sums for each:
    # t=1: 0 + min(4999999,5000001)=4999999 + min(9999999,1)=1 + min(2499999,7500001)=2499999 + min(7499999,2500001)=2500001 =4999999+1+2499999+2500001=10000000
    # t=5000000: min(4999999,5000001)=4999999 +0 + min(5000000,5000000)=5000000 + min(2500000,7500000)=2500000 + min(2500000,7500000)=2500000=4999999+5000000+2500000+2500000=15000000
    # t=10000000: min(9999999,1)=1 + min(5000000,5000000)=5000000 +0 + min(7500000,2500000)=2500000 + min(2500000,7500000)=2500000=1+5000000+0+2500000+2500000=10000001
    # t=2500000: min(2500000-1=2499999,7500001)=2499999 + min(5000000-2500000=2500000,7500000)=2500000 + min(10000000-2500000=7500000,2500000)=2500000 +0 + min(7500000-2500000=5000000, 5000000)=5000000=2499999+2500000+2500000+0+5000000=12500000-1=12499999
    # t=7500000: similar calculations
    # Minimal sum is 10000000
    print(minTime(inArr4))  # Expected Output: 10000000

    # Test Case 5: Multiple disks with the same position
    inArr5 = [6, 100, 100, 100, 100, 100, 100]
    print(minTime(inArr5))  # Expected Output: 0

    # Test Case 6: Near wrap-around
    inArr6 = [3, 9999999, 7, 9999995]
    # Align to 9999999: 0 + min(9999999-7=9999992,10_000_000-9999992=8) + min(9999995-9999999=4,10_000_000-4=9999996)=0+8+4=12
    # Align to 7: min(9999999-7=9999992,min=8) +0 + min(9999995-7=9999988,min=12)=8+0+12=20
    # Align to 9999995: min(9999995-9999999=4,min=9999996)=4 + min(9999995-7=9999988,min=12)+ min(9999995-9999995=0)=4+12+0=16
    # Minimal sum is 12
    print(minTime(inArr6))  # Expected Output: 12
