class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dist = float('inf')
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]
                curr_dist = abs(target - total)
                closest_dist = abs(target - dist)

                if curr_dist < closest_dist:
                    dist = total 

                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    return total
            
        return dist

        
        