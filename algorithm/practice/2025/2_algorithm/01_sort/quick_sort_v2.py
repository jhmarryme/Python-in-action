import random


def quick_sort_basic(arr):
    """
    2. 优化 1：随机选择基准（Random Pivot）
    优化点：随机选择基准元素，避免有序数组下的最坏情况，使期望时间复杂度稳定在 O(nlogn)。
    核心：通过random.choice随机选基准，而非固定第一个元素。
    """
    if len(arr) <= 1:
        return arr
    # 随机选择基准，避免有序数组退化
    pivot = random.choice(arr)
    # 单独处理相等元素，减少递归次数
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_basic(left) + mid + quick_sort_basic(right)


arr = [3, 4, 1, 2, 6, 7]
print(arr)
print(quick_sort_basic(arr))

arr = [random.randint(1, 100) for _ in range(20)]
print(arr)
print(quick_sort_basic(arr))
