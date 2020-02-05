# class Solution:
#     def maxSubArray(self, nums: 'List[int]') -> 'int':
#         n = len(nums)
#         curr_sum = max_sum = nums[0]

#         for i in range(1, n):
#             curr_sum = max(nums[i], curr_sum + nums[i])
#             max_sum = max(max_sum, curr_sum)
            
#         return max_sum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)
