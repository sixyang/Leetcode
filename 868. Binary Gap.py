class Solution:
    def binaryGap(self, N: int) -> int:
        n = bin(N)
        maximum = 0
        for index, element in enumerate(n):
            if element == '1':
                follows = n[index+1:]
                if '1' in follows:
                    next1 = follows.index('1') + 1
                    if maximum < next1:
                        maximum = next1              
        return maximum 
