import math


def find_number(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n >= 1000000:
        return 0
    sequence = [1, 2]
    seen = {1, 2}

    current = 2
    failed = False
    while True:
        for num in range(3, 1000000):
            if num >= 1000000:
                failed = True
                break
            if num not in seen and math.gcd(current, num) > 1:
                sequence.append(num)
                seen.add(num)
                current = num
                break
        if failed:
            return 0
        if current == n:
            return len(sequence)
