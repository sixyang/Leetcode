class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            if n % 4 == 0:
                n //= 4
            else:
                return False
        return True if n > 0 else False
