/**
 * @param {number[]} nums
 * @return {number}
 */
var dominantIndex = function(nums) {
    let max = 0;
    for (var i in nums){
        if (nums[i] > max) max = nums[i];
    }
    max_index = nums.indexOf(max);
    numss = nums.slice(0,max_index).concat(nums.slice(max_index+1,nums.length))
    for (let j in numss){
        if (2*numss[j] > max) return -1
    }return max_index;
};
