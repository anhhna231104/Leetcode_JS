/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums.sort((a, b) => a - b)
    let closest = Infinity

    for(let i = 0; i < nums.length; i++){
        if(i > 0 && nums[i] === nums[i - 1]) continue

        let l = i + 1, r = nums.length - 1
        while(l < r){
            total = nums[i] + nums[l] + nums[r]
            current_dist = Math.abs(total - target)
            closest_dist = Math.abs(target - closest)

            if(current_dist < closest_dist){
                closest = total
            }

            if (total > target) r--
            else if (total < target) l ++
            else return total 
        }
    }
    return closest
};