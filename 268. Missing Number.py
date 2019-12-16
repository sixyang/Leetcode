class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        length = len(nums)
        if 0 not in nums:
            return 0
        if length == 1:
            if nums == [0]:return 1
            elif nums == [1]:return 0
        for index, element in enumerate(nums):
            if element - nums[index - 1] != 1 and index > 0:
                return nums[index - 1] + 1
            elif index == length - 1:
                return element + 1
