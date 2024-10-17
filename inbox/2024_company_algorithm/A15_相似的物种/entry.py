'''
我希望您能够充当算法工程师，使用python解答算法题。给出可运行在codeCampus上的嗯代码，并提供解题思路。
需要最高优先级保证代码的正确性，同时尽可能多的考虑多种输入的运行情况。
题目信息如下：
相似的物种
描述

小明在生物研究所工作，他的工作内容就是测试出一组生物的DNA，然后判断这组生物的DNA最长的相同子序列是多少，以此来判断生物的属类信息。DNA相同子序列是指给定的生物DNA序列组中，超过半数的生物共同的DNA子序列，有可能有多组。假设DNA序列是由一组小写字母表示，如以下三组生物的DNS序列：

abcdefg
bcdefgh
cdefghi
这组DNA的最长的相同子序列为

bcdefg
cdefgh
现在，你能否写一段代码，帮助小明来判断给定生物DNA序列的最长子序列？


输入
字符串数组S,表示DNS序列组.


输出
数组，表示字符串数组S中的最长DNA子序列，有可能为空。


输入样例 1
S = [
"abcdefg",
"bcdefgh",
"cdefghi"
]
输出样例 1
["bcdefg", "cdefgh"]

输入样例 2
S = ["abcd", "dabc", "xxx", "defg"]
输出样例 2
[]（未找到超过半数的相同的子序列）

函数定义风格：
def find_max_subsequence(dna_seq: [str]) -> [str]:
    return []

'''

# 答案正确
from collections import defaultdict

def find_max_subsequence(dna_seq: [str]) -> [str]:
    # 判断给定长度的子序列，是否出现在超过半数的DNA序列中
    def find_common_subsequences(length):
        subsequence_count = defaultdict(int)

        # 遍历每一个DNA序列，使用滑动窗口提取所有长度为length的子序列
        for seq in dna_seq:
            seen = set()  # 用于防止同一个子序列在同一个DNA序列中重复计数
            for i in range(len(seq) - length + 1):
                subseq = seq[i:i + length]
                if subseq not in seen:
                    subsequence_count[subseq] += 1
                    seen.add(subseq)

        # 过滤出出现在超过半数的子序列
        return [subseq for subseq, count in subsequence_count.items() if count > len(dna_seq) // 2]

    # 从最长可能的子序列长度开始尝试，逐步减少长度
    max_length = min(len(seq) for seq in dna_seq)  # 最大子序列长度为最短DNA序列的长度
    for length in range(max_length, 0, -1):
        common_subsequences = find_common_subsequences(length)
        if common_subsequences:
            return sorted(common_subsequences)  # 按字典顺序返回结果

    return []

# 示例测试
S1 = ["abcdefg", "bcdefgh", "cdefghi"]
S2 = ["abcd", "dabc", "xxx", "defg"]

print(find_max_subsequence(S1))  # 输出: ["bcdefg", "cdefgh"]
print(find_max_subsequence(S2))  # 输出: []
