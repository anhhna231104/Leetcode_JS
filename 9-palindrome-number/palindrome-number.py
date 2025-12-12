class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        n = x
        total = 0
        while n > 0:
            tmp = n % 10
            total = total*10 + tmp
            n //= 10

        return x == total