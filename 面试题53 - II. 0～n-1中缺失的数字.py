class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     if nums[i] != i: return i
        # return i+1

        # 果然二分还是爽啊！而且这个二分还是挺明显的~
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > mid: r = mid
            else: l = mid + 1
        return nums[l] - 1 if nums[l] != l else nums[l] + 1
