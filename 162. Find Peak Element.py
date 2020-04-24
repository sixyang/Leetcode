class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # return nums.index(max(nums))

        # 这个是看了别人的代码之后做出来的，感觉比较神奇，估计需要思考一段时间才能想到~
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left
