class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = True if x < 0 else False
        n = abs(x)
        res = 0

        while n > 0:
            tmp = n % 10
            res = res*10 + tmp
            n //= 10

        if res > 2**31 - 1 or res < -2**31:
            return 0
        return -res if negative else res
