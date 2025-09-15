class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        p, q, r = 0, 1, 0
        for i in range(2, n + 1):
            r = p + q
            p, q = q, r
        return r
