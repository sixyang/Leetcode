class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        li = {2 ** i for i in range(40)}
        if n in li:
            return True
        else:
            return False
            
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0            
