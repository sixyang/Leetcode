class Solution:
    def isUgly(self, num: int) -> bool:
        while num > 0:
            if num % 2 == 0:
                num = num // 2
                continue
            elif num % 3 == 0:
                num = num // 3
                continue
            elif num % 5 == 0:
                num = num // 5
                continue
            elif num == 1:
                return True
            else:
                return False
