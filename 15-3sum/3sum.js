/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a, b) => a - b)
    let res = []

    for(let i = 0; i < nums.length; i++)
    {
        if (i > 0 && nums[i] == nums[i - 1]) continue

        l = i + 1, r = nums.length - 1
        while (l < r)
        {
            total = nums[i] + nums[l] + nums[r]

            if (total < 0) l += 1
            else if (total > 0) r -= 1
            else {
                res.push([nums[i], nums[l], nums[r]])
                l += 1
                while (nums[l] == nums[l - 1] && l < r)
                    l += 1
            }          
        }
    }

    return res
};