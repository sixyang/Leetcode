class Solution:
    def trailingZeroes(self, n: int) -> int:
        fives = 5
        nums = 0
        while n >= fives:
            nums += n // fives
            fives *= 5
        return nums
