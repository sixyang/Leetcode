class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        a = int(''.join([str(i) for i in A]))
        ret = a + K
        return list(str(ret))
