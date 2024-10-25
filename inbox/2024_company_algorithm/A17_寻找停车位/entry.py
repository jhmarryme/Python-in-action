'''
我希望您能够充当算法工程师，使用python解答算法题。给出可运行在codeCampus上的嗯代码，并提供解题思路。
需要最高优先级保证代码的正确性，同时尽可能多的考虑多种输入的运行情况。

题目信息如下：
接收一个整数数组n, n代表一个数轴, 每个元素代表数轴上的一个点,
从一个任意的点x(不一定是n中的元素) 开始依次访问数轴上的所有点, 最后回到x点
如 x=9, 从9访问 10, 再从10 访问 20, 最后从20回到9

如 [24,13, 27]
找到一个合适的数字x, 从x开始访问每个元素, 如x=10, 可以选择先访问13(行走距离为3), 再从13访问24(距离为11), 再从24访问27, 最后回到x(距离17) 本次行走距离总和y=34

请你帮忙找到一个合适的距离点x, 使其行走距离之和y最小,即行走路径最短

输入
数组n，0 ≤ ni ≤ 99

输出
最小距离y

输入样例
[24 13 89 37]

输出样例
152

函数定义风格：
def minDistance(inArr):
    return 0



# 补充提问:
你需要x开始依次访问每个点, 而不是计算x和每个点的距离之和
'''
# 答案正确
def minDistance(inArr):
    inArr.sort()

    min_point = min(inArr)
    max_point = max(inArr)

    min_total_distance = float('inf')

    for x in range(min_point, max_point + 1):
        total_distance = 0
        current_pos = x

        for point in inArr:
            total_distance += abs(current_pos - point)
            current_pos = point

        total_distance += abs(current_pos - x)

        min_total_distance = min(min_total_distance, total_distance)

    return min_total_distance

# 测试
print(minDistance([24, 13, 89, 37]))  # 输出应为 152
