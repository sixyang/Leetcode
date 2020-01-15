class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        S = list(S)
        left = S.index(C)
        right = len(S) - (S[::-1].index(C)) - 1
        ret = []
        for index, element in enumerate(S):
            if element == C:
                ret.append(0)
                S[index] = None
                if C in S:
                    right = S.index(C)
                left = index
            else:
                ret.append(min(abs(index - left), abs(right - index))) 
        return ret
                
