import math


def find_path_number(m: int, n: int) -> str:
    if m < 1 or n < 1:
        return 0

    total_steps = (m - 1) + (n - 1)
    steps_down = m - 1

    try:
        path_count = math.comb(total_steps, steps_down)
    except AttributeError:
        def comb(n, k):
            if k < 0 or k > n:
                return 0
            if k == 0 or k == n:
                return 1
            k = min(k, n - k)
            result = 1
            for i in range(1, k + 1):
                result = result * (n - k + i) // i
            return result

        path_count = comb(total_steps, steps_down)

    return path_count


# =============================
# 测试用例
# =============================
if __name__ == "__main__":
    # 测试用例 1: 示例输入
    m1, n1 = 3, 3
    print(find_path_number(m1, n1))  # 预期输出: "P=6"

    # 测试用例 2: 单行
    m2, n2 = 1, 5
    print(find_path_number(m2, n2))  # 预期输出: "P=1"

    # 测试用例 3: 单列
    m3, n3 = 5, 1
    print(find_path_number(m3, n3))  # 预期输出: "P=1"

    # 测试用例 4: 较大网格
    m4, n4 = 10, 10
    print(find_path_number(m4, n4))  # 预期输出: "P=48620"

    # 测试用例 5: 最小网格
    m5, n5 = 1, 1
    print(find_path_number(m5, n5))  # 预期输出: "P=1"

    # 测试用例 6: 不对称网格
    m6, n6 = 4, 5
    print(find_path_number(m6, n6))  # 预期输出: "P=35"

    # 测试用例 7: 较大值
    m7, n7 = 20, 20
    print(find_path_number(m7, n7))  # 预期输出: "P=35345263800"

    # 测试用例 8: 边界输入
    m8, n8 = 0, 5
    print(find_path_number(m8, n8))  # 预期输出: "P=0"
