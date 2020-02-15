/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
 //差不多的代码，JS超过94%，而python超过9%，啧啧，这题目还是蛮简单的。标准双指针~
var twoSum = function(numbers, target) {
    let l = 0, r = numbers.length-1, ret = 0;
    while (l < r){
        let sum = numbers[l] + numbers[r];
        if (sum < target) l += 1;
        else if (sum > target) r -= 1;
        else return [l+1, r+1];
    } 
    
};
