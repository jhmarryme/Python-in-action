from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        # 优化点: 有效字符串的长度一定为偶数
        if len(s) % 2 != 0:
            return False
        left = ['(', '{', '[']
        right = [')', '}', ']']
        stack = deque()
        for sign in s:
            if sign in left:
                stack.append(right[left.index(sign)])
            elif sign in right:
                if len(stack) == 0:
                    return False
                if stack.pop() != sign:
                    return False

        return len(stack) == 0


s = '([)]'

print(Solution().isValid(s))
