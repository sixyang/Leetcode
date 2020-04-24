class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        # return sorted(nums)[0]

        # 这里将整个列表分成两部分：大于最后一个值的，小于最后一个值的。 于是就变成了 最初的错误版本 题目。
        left, right, last = 0, len(nums) - 1, nums[-1]
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > last:
                left = middle + 1
            elif nums[middle] <= last:
                right = middle
        return nums[left]
