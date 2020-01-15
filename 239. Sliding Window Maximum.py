class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:return nums
        ret = []
        for index, element in enumerate(nums[:len(nums)-k+1]):
            temp = nums[index: index+k]
            ret.append(max(temp))
        return ret
