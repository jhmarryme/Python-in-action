import random


def merge_sort_in_place(arr):
    if len(arr) <= 1:
        return arr
    merge_sort(arr, 0, len(arr) - 1)
    return arr


def merge_sort(arr, left, right):
    if left >= right:
        return
    mid = left + right // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge_in_place(arr, left, mid, right)


def merge_in_place(arr, left, mid, right):
    pass


arr = [3, 4, 1, 2, 6, 7]
print(arr)
print(merge_sort_in_place(arr))

arr = [random.randint(1, 100) for _ in range(20)]
print(arr)
print(merge_sort_in_place(arr))
