class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            if n % 3 == 0:
                n = n // 3
            else:
                return False
        return True if n > 0 else False
