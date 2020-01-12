class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J = set(J)
        quantities = 0
        for i in S:
            if i in J:
                quantities += 1
        return quantities
