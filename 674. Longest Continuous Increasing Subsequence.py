class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:return 0
        len_nums = len(nums)
        length, length2 = (1, 1)
        for i in range(1, len_nums):
            if nums[i] > nums[i-1]:
                length2 += 1
            else:
                length2 = 1
            length = max(length, length2)
        return length
