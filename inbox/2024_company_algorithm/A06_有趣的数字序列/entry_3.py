import math

def find_number(n: int) -> int:
    """
    Computes the position k of number n in the "Interesting Number Sequence".
    Returns 0 if n is not in the sequence.

    Sequence Rules:
    - First two terms are 1 and 2.
    - Each subsequent term is the smallest unused positive integer that shares a common divisor (>1) with the previous term.
    """
    if n < 1 or n >= 1000000:
        # Out of valid range
        return 0

    if n == 1:
        return 1
    if n == 2:
        return 2

    max_num = 1000001  # Define a limit to prevent infinite loops
    used = [False] * (max_num + 1)
    used[1] = True
    used[2] = True

    # Initialize the Smallest Prime Factor (SPF) array using Sieve of Eratosthenes
    spf = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        if spf[i] == 0:
            spf[i] = i
            for multiple in range(i * 2, max_num + 1, i):
                if spf[multiple] == 0:
                    spf[multiple] = i

    # Initialize next_multiple list where next_multiple[p] = p initially
    # Since p >=2, list index 0 and 1 are unused
    next_multiple = list(range(max_num + 1))  # next_multiple[p] = p

    current = 2
    position = 2

    while position < max_num:
        # Retrieve unique prime factors of the current number
        c = current
        factors = set()
        while c > 1:
            p = spf[c]
            factors.add(p)
            while c % p == 0:
                c //= p

        # Collect candidate numbers from all prime factors
        candidates = []
        for p in factors:
            m = next_multiple[p]
            # Find the smallest multiple of p that is unused
            while m <= max_num and used[m]:
                m += p
            if m > max_num:
                continue  # No valid multiple found within range
            if not used[m]:
                candidates.append(m)
                next_multiple[p] = m + p  # Update the pointer for prime p

        if not candidates:
            break  # No further candidates can be added; terminate early

        # Select the smallest candidate as the next number in the sequence
        x = min(candidates)

        # Increment position
        position += 1

        if x == n:
            return position

        # Mark the number as used and update current
        used[x] = True
        current = x

    # If n was not found in the sequence, return 0
    return 0

# =============================
# Example Test Cases
# =============================

if __name__ == "__main__":
    # Test Case 1: Sample Input 1
    n1 = 999999
    print(find_number(n1))  # Expected Output: 10

    # Test Case 2: Number 1
    n2 = 1
    print(find_number(n2))  # Expected Output: 1

    # Test Case 3: Number 2
    n3 = 2
    print(find_number(n3))  # Expected Output: 2

    # Test Case 4: Number 3
    n4 = 3
    print(find_number(n4))  # Expected Output: 5

    # Test Case 5: Number 4
    n5 = 4
    print(find_number(n5))  # Expected Output: 3

    # Test Case 6: Number 6
    n6 = 6
    print(find_number(n6))  # Expected Output: 4

    # Test Case 7: Number 9
    n7 = 9
    print(find_number(n7))  # Expected Output: 6

    # Test Case 8: Number 12
    n8 = 12
    print(find_number(n8))  # Expected Output: 7

    # Test Case 9: Number 7
    n9 = 7
    print(find_number(n9))  # Expected Output: 14

    # Test Case 10: Number 10
    n10 = 10
    print(find_number(n10))  # Expected Output: 9

    # Test Case 11: Number 16
    n11 = 16
    print(find_number(n11))  # Expected Output: 17

    # Test Case 12: Number 15
    n12 = 15
    print(find_number(n12))  # Expected Output: 11

    # Test Case 13: Number not in sequence
    n13 = 11
    print(find_number(n13))  # Expected Output: 0 (Assuming 11 is not in the sequence)

    # Test Case 14: Number beyond the sample sequence
    n14 = 20
    print(find_number(n14))  # Expected Output: Position based on the sequence