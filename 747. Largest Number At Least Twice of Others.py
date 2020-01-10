class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maximum = max(nums)
        m_index = nums.index(maximum)
        nums.remove(maximum)
        for i in nums:
            if i * 2 > maximum:
                return -1
        return m_index
