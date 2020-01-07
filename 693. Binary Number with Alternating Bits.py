class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n)
        for i in range(2, len(binary)):
            if binary[i] == binary[i - 1]:
                return False
        return True
            
