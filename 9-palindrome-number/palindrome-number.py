class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        n = x
        rev = 0
        while n > 0:
            tmp = n % 10
            rev = rev*10 + tmp
            n //= 10
        
        return rev == x