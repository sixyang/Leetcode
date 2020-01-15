class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            position = nums.index(target)
        except Exception as e:
            return -1
        else:
            return position
