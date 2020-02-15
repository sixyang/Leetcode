/**
 * @param {number[]} nums
 * @return {number}
 */
 //Js里面的排序默认是按照ascii进行排序的，所以对于负数，会出现顺序相反的结果。。。噫，太坑了。
var arrayPairSum = function(nums) {
    nums.sort(function(a,b){return a-b;});
    let ret = 0;
    for (let i in nums){
        if (i % 2 == 0) ret += nums[i];
    }return ret;
};
