'''
我希望您能够充当算法工程师，使用python解答算法题。给出可运行在codeCampus上的嗯代码，并提供解题思路。
需要最高优先级保证代码的正确性，同时尽可能多的考虑多种输入的运行情况。
题目信息如下：
变速自行车前后各有一个带有多个链轮的齿轮，假设前面有三个链轮，后面有九个链轮。骑行人会选择一个前面的链轮和一个后面的链轮。

比率（前面链轮齿数/后面链轮齿数）给出了齿轮骑行的相对难度。齿轮配置通常以比率的形式给出。例如，42/21表示前面有一个42齿的链轮，后面有一个21齿的链轮。

转动齿轮的难易程度也取决于后轮的大小。当比率乘以后轮的周长时，我们就得到了该特定自行车上齿轮大小的度量。

例如，一个直径为27英寸的轮子其周长为84.82293英寸（如果我们使用3.14159作为π的近似值）。比率=52/15，齿轮大小=(52/15) * 84.82293 = 294.052824

问题：当知道目标齿轮大小后，如何设置比率计算出的齿轮大小最接近目标值


输入
数组： 包含14个元素：f1 f2 f3 r1 ... r9 diameter target

其中f1 < f2 < f3 是三个前链轮，r1 < r2 < ... < r9 是九个后链轮，diameter 是轮子的直径，target 是目标齿轮大小


输出
数组：包含两个元素： [a,b]

a:前链轮

b:后链轮

说明：最接近的目标齿轮大小, 四舍五入到小数点后三位 （π = 3.14159） 如果有多个最接近的大小，则取前链轮最小的比率组合


输入样例
[32 42 52 12 13 14 15 16 17 21 24 27 27 294]
输出样例
[52 15]

函数定义风格:
def calGearSize(inArr):
    return []


'''


def calGearSize(inArr):
    f = inArr[:3]
    r = inArr[3:12]
    diameter = inArr[12]
    target = inArr[13]

    pi = 3.14159
    circumference = pi * diameter

    min_diff = float('inf')
    best_combo = [0, 0]

    for front in f:
        for rear in r:
            ratio = front / rear
            gear_size = ratio * circumference
            diff = abs(gear_size - target)

            if diff < min_diff or (diff == min_diff and front < best_combo[0]):
                min_diff = diff
                best_combo = [front, rear]

    return best_combo


# 测试用例
input_data = [32, 42, 52, 12, 13, 14, 15, 16, 17, 21, 24, 27, 27, 294]
print(calGearSize(input_data))  # 输出 [52, 15]
