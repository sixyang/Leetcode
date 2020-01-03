class Solution:
    def convertToBase7(self, num: int) -> str:
        num7 = ''
        negative = False
        if num < 0:
            negative = True
        num = abs(num)
        while num >= 7:
            mod = num % 7
            num7 = ''.join([str(mod), num7])
            num //= 7
            if num < 7:
                num7 = ''.join([str(num), num7])
                return num7 if not negative else ''.join(['-',num7])
        return str(num) if not negative else ''.join(['-',str(num)])
