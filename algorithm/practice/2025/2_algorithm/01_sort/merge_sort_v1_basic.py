import random


def merge_sort_basic(arr):
    """
    1. 基础版本（Naive Merge Sort）
    核心思路：分治策略，将数组分为两半，递归排序后合并两个有序子数组。
    缺点：需要额外的O(n)辅助空间存储合并结果，递归开销较大。
    """
    if len(arr) <= 1:
        return arr
    # 分治：拆分为左右两半
    mid = len(arr) // 2
    left = merge_sort_basic(arr[:mid])
    right = merge_sort_basic(arr[mid:])
    # 合并两个有序子数组
    return merge(left, right)


def merge(left, right):
    """
    python有一个模块，专门提供了归并排序的方法，叫做“heapq”模块, 这个merge方法可以不用手写
    from heapq import merge
    """
    # 不需要判断也行
    # if len(left) == 0 or len(right) == 0:
    #     return left + right
    point_1, point_2 = 0, 0
    res = []
    while point_1 < len(left) and point_2 < len(right):
        if left[point_1] < right[point_2]:
            res.append(left[point_1])
            point_1 += 1
        else:
            res.append(right[point_2])
            point_2 += 1
    res.extend(right[point_2:])
    res.extend(left[point_1:])
    return res


arr = [3, 4, 1, 2, 6, 7]
print(arr)
print(merge_sort_basic(arr))

arr = [random.randint(1, 100) for _ in range(20)]
print(arr)
print(merge_sort_basic(arr))
