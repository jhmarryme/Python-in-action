import random


def quick_sort_basic(arr):
    """
    1. 基础版本（Naive Quick Sort）
    核心思路：选择数组第一个元素作为基准（pivot），通过分区（partition）将数组分为 “小于基准” 和 “大于基准” 两部分，递归排序子数组。
    缺点：对有序 / 近乎有序数组，基准选择极差，时间复杂度退化为 O(n²)。
    """
    if len(arr) <= 1:
        return arr
    # 选择第一个元素为基准
    pivot = arr[0]
    # 分区：小于基准的放左边，大于的放右边
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    # 递归排序并合并
    return quick_sort_basic(left) + [pivot] + quick_sort_basic(right)


arr = [3, 4, 1, 2, 6, 7]
print(arr)
print(quick_sort_basic(arr))

arr = [random.randint(1, 100) for _ in range(20)]
print(arr)
print(quick_sort_basic(arr))
