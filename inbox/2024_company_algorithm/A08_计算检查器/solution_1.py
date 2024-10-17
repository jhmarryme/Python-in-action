"""
计算检查器
描述
小军是一个10岁的程序员，最近他完成了一个程序，可以计算出一个整数数组中指定位置闭区间[i, j]的所有整数和v。他的爸爸发现小军写的程序中有一个BUG，程序在多次计算之后会因为一些条件导致计算结果错误。
幸运的是小军的每次计算过程都记录了区间位置[i, j]及和v的信息，不幸的是小军没有记录整数数组的信息。于是，小军的爸爸决定依据于小军程序的记录信息写一个程序来检查哪些计算结果出了问题。
由于小军的程序没有记录整数数组的信息，小军爸爸的检查程序只能依赖于区间位置[i, j]及整数和v的信息，所以小军爸爸假设第一次出现的记录结果都是正确的，后续的记录结果依据于前面的正确结果来检验。
如，小军的一次运行程序产生以下记录结果：
     i   j   v
第1行 1   2   1
第2行 1   2   2
第3行 5   6   3
第4行 1   6   7
第5行 3   4   50
第6行 7   10  10
小军爸爸的程序应该给出检查结果如下：
第1行：correct
第2行：wrong --> 与第1行的冲突
第3行：correct
第4行：correct
第5行：wrong --> 通过第4行减去第3行的计算结果，再减去第一行的计算结果获取，应该为3
第6行：correct

请你完成小军爸爸想写的程序来帮助检查小军程序计算结果是否正确。

输入
小军程序运行的记录数据records，records为一个二维数组，3列值，第1列值为计算区间开始位置i,第2列值为计算区间结束位置j，第3列值为计算和v。

输出
输出一个整数数组，数组大小应该为records的行数，每一个值表示records中对应行的检查结果，如果计算结果正确，设置为0，如果计算结果错误，设置为正确的结果。

输入样例
records = [
[1, 2, 1],
[1, 2, 2],
[5, 6, 3],
[1, 6, 7],
[3, 4, 50],
[7, 10, 10]
]
输出样例
[0, 1, 0, 0, 3, 0]

函数定义风格如下:
def find_bugs(records: [[int]]) -> []:
    # :param records: 小军程序运行的记录数据，3列值，第1列值为计算区间开始位置i,第2列值为计算区间结束位置，第3列值为计算和。
    # :return: 输出一个整数数组，数组大小应该为records的行数，每一个值表示records中对应行的检查结果，如果计算结果正确，设置为0，如果计算结果错误，设置为正确的结果。
    return []
"""


# 部分正确, 差一分
def find_bugs(records: [[int]]) -> []:
    """
    :param records: 小军程序运行的记录数据，3列值，第1列值为计算区间开始位置i, 第2列值为计算区间结束位置j, 第3列值为计算和v。
    :return: 输出一个整数数组，数组大小应该为records的行数，每一个值表示records中对应行的检查结果，
             如果计算结果正确，设置为0，如果计算结果错误，设置为正确的结果。
    """

    class UnionFind:
        def __init__(self, size):
            self.parent = list(range(size))
            self.weight = [0] * size

        def find(self, x):
            if self.parent[x] != x:
                orig_parent, orig_weight = self.find(self.parent[x])
                self.parent[x] = orig_parent
                self.weight[x] += orig_weight
            return self.parent[x], self.weight[x]

        def union(self, x, y, v):
            root_x, w_x = self.find(x)
            root_y, w_y = self.find(y)
            if root_x == root_y:
                # Check if the current relationship satisfies the new sum
                return (w_y - w_x) == v
            else:
                # Merge the sets and adjust the weight accordingly
                self.parent[root_x] = root_y
                self.weight[root_x] = w_y - w_x - v
                return True

    if not records:
        return []

    # Determine the maximum index needed
    max_j = max(record[1] for record in records)
    size = max_j + 1  # Since we need to include index j

    uf = UnionFind(size)
    result = []

    for record in records:
        i, j, v = record
        x = i - 1  # Convert to 0-based index for S[i-1]
        y = j  # Convert to 0-based index for S[j]

        # Ensure indices are within bounds
        if x < 0:
            x = 0

        # Check if indices are within the initialized size
        if y >= size:
            # Extend the UnionFind structure if needed
            additional = y - size + 1
            uf.parent.extend(range(size, size + additional))
            uf.weight.extend([0] * additional)
            size += additional

        is_correct = uf.union(x, y, v)
        if is_correct:
            result.append(0)
        else:
            # If there is a conflict, determine the correct sum
            root_x, w_x = uf.find(x)
            root_y, w_y = uf.find(y)
            if root_x == root_y:
                correct_v = w_y - w_x
                result.append(correct_v)
            else:
                # If they are not connected, theoretically it shouldn't happen
                # since we just tried to union them. But to be safe:
                result.append(v)  # Assuming the given v is correct in this ambiguous case

    return result


if __name__ == "__main__":
    records = [
        [1, 2, 1],
        [1, 2, 2],
        [5, 6, 3],
        [1, 6, 7],
        [3, 4, 50],
        [7, 10, 10]
    ]
    print(find_bugs(records))  # 输出: [0, 1, 0, 0, 3, 0]
