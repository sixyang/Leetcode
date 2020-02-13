/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let sum = 0;
    for (let i of nums){
        sum += i;
    }
    let left = 0;
    for (let j in nums){
        if (left == sum - left - nums[j]){
            return j;
        }
        left += nums[j];
    }
    return -1;
};
