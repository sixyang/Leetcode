class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret = 0
        num = 0
        rets = []
        i = 0
        while i < len(nums):
            if ret | nums[i] == 1:
                num += 1
            else:
                rets.append(num)
                num = 0
            i += 1
        rets.append(num)
        return max(rets)
