def nextSeq(inArr):
    f0, f1, f2 = inArr

    C = f0
    
    A_plus_B = f1 - C
    A = (f2 - C - 2 * A_plus_B) / 2
    B = A_plus_B - A

    result = [int(A * x**2 + B * x + C) for x in range(3, 6)]
    
    return result

# 示例测试
print(nextSeq([1, 2, 3]))  # 应输出 [4, 5, 6]