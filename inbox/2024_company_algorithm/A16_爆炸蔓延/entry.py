'''
我希望您能够充当算法工程师，使用python解答算法题。给出可运行在codeCampus上的嗯代码，并提供解题思路。
需要最高优先级保证代码的正确性，同时尽可能多的考虑多种输入的运行情况。
题目信息如下：

买买提家里有一片牧场，某天他发现牧场内有很多的树桩（可能是前几天暴风雨过后摧毁了大片树林），这些树桩都是排成一行的，且每个树桩都有特定的高度。

买买提想使用特制炸药来清理这些树桩，这种特制炸药能够摧毁相邻的树桩，前提是这些相邻的树桩严格低于最近被摧毁的树桩。如果接下来相邻的树桩比刚刚被摧毁的树桩更矮，

那么爆炸波可以继续向更远的相邻树桩蔓延。然而，一旦遇到的树桩不比前一个更矮，该方向上的破坏就会停止（目标树桩的另一侧遵循相同的规则）。

例如考虑一排九棵树桩，它们的高度如下：

1 2 5 4 3 3 6 6 2

如果买买提炸毁第三棵树桩（高度为 5），那么第二棵树桩（高度为 2）也会被摧毁，第一棵树桩（高度为 1）同样会被摧毁。

类似地，第四棵树桩（高度为 4）和第五棵树桩（高度为 3）也会因为依次更矮而被摧毁，剩下的树桩排列如下：
* * * * * 3 6 6 2

再使用两次炸药（在第 7 和第 8 棵树桩处）就可以摧毁剩余的所有树桩。
请帮助买买提确任如何爆破树桩，使得消耗的炸药最少。


输入
数组n：数组长度为树桩总数，范围（1～10000），每个数组元素代表该树桩的高度

输出
输出一个数组，每个元素代表需要炸毁的树桩的索引（索引从1开始），输出时请按照元素从小到大排序


输入样例
[1 2 5 4 3 3 6 6 2]

输出样例
[3 7 8]


函数定义风格：def blowUp(inArr):
    return []
'''

# 答案正确
def blowUp(inArr):
    n = len(inArr)
    destroyed = [False] * n  # 记录树桩是否已经被摧毁
    result = []  # 记录需要爆破的树桩索引
    indices = list(range(n))  # 存储树桩的索引

    # 按照树桩的高度从高到低排序
    indices.sort(key=lambda x: -inArr[x])

    for idx in indices:
        if destroyed[idx]:
            continue  # 如果该树桩已经被摧毁，跳过

        # 将当前树桩加入结果，注意结果要求的是1开始的索引
        result.append(idx + 1)

        # 向左摧毁
        left = idx - 1
        while left >= 0 and inArr[left] < inArr[left + 1] and not destroyed[left]:
            destroyed[left] = True
            left -= 1

        # 向右摧毁
        right = idx + 1
        while right < n and inArr[right] < inArr[right - 1] and not destroyed[right]:
            destroyed[right] = True
            right += 1

        # 标记当前树桩为已摧毁
        destroyed[idx] = True

    result.sort()  # 按照索引升序输出
    return result
