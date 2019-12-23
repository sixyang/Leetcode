class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length = len(nums_set)
        if length == 0:
            return []
        elif 0 < length < 3:
            return max(nums)
        else:
            nums = sorted(nums_set)
            return nums[-3]
            
