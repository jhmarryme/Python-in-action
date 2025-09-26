import random


def insertion_sort_basic(arr):
    """
    核心思路类比整理扑克牌：
        将数组分为 “已排序区” 和 “未排序区”，每次从 “未排序区” 取一个元素，插入到 “已排序区” 的合适位置，直到整个数组有序。
    特点：稳定排序（相等元素相对位置不变）、原地排序（仅需O(1)额外空间）
    """
    if len(arr) <= 1:
        return arr
    # 从第二个元素开始（第一个元素默认在已排序区）
    for i in range(1, len(arr)):
        # key: element to sort
        key = arr[i]
        # compare with previous element first
        j = i - 1
        # 在已排序区中找到插入位置：将大于key的元素向后移
        while j >= 0 and arr[j] > key:
            # 元素后移
            arr[j + 1] = arr[j]
            j -= 1
        # 插入key到正确位置
        arr[j + 1] = key
    return arr


arr = [3, 4, 1, 2, 6, 7]
print(arr)
print(insertion_sort_basic(arr))

arr = [random.randint(1, 100) for _ in range(20)]
print(arr)
print(insertion_sort_basic(arr))
