class Solution:
    def sumZero(self, n: int) -> List[int]:
        ret = []
        if n & 1 == 1:
            ret.append(0)  
        for i in range(n//2):
                ret.extend([i+1, -i-1])
        return ret
