# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            middle = (left + right) // 2
            num = guess(middle)
            if num == -1:
                right = middle              # 我就把这儿的 right=middle-1 改成了right=middle，性能提升80%，啧啧，
            elif num == 1:
                left = middle + 1
            else: return middle
