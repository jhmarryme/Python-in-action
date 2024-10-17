def find_bugs(records: [[int]]) -> []:
    # 用于存储有效的计算结果，同时这里使用较大的数保留可能状态
    max_length = 10**5  # 假设10^5大小的最大可能区间
    sum_array = [None] * (max_length + 1)
    results = []

    for index, (i, j, v) in enumerate(records):
        actual_sum = sum_array[i:j + 1].count(None) * None  # 计算当前和

        # 计算当前和
        current_sum = 0
        for k in range(i, j + 1):
            if sum_array[k] is not None:
                current_sum += sum_array[k]

        # 计算区间的总值的数量
        values_counted = sum(1 for k in range(i, j + 1) if sum_array[k] is not None)

        # 如果有未知的数量，那么需要更进一步的判断
        if values_counted < (j - i + 1):
            # 如果这个是第一次我们见到的，直接设置值
            if index == 0 or sum_array[i] is None or sum_array[j] is None:
                for k in range(i, j + 1):
                    if sum_array[k] is None:
                        sum_array[k] = 0
                sum_array[j] = sum_array[j] if sum_array[j] is not None else v - current_sum + 0
            results.append(0)
        else:
            if current_sum < v:
                # 只在计算已经确定的情况下才能判断
                results.append(v - current_sum)
            else:
                if current_sum == v:
                    results.append(0)
                else:
                    results.append(current_sum)

    return results

# 测试样例
records = [
    [1, 2, 1],
    [1, 2, 2],
    [5, 6, 3],
    [1, 6, 7],
    [3, 4, 50],
    [7, 10, 10]
]

print(find_bugs(records))  # 输出 [0, 1, 0, 0, 3, 0]