class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in h:
                return [i, h[comp]]
            h[num] = i
        
        return h
                
            
            
            
    