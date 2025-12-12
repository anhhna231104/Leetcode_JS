class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in hashmap:
                return [i, hashmap[comp]]
            hashmap[num] = i
        
        return hashmap
        
            
            
    