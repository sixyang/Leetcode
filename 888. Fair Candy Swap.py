class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sub = sum(A) - sum(B)
        A = set(A)
        B = set(B)
        for i in B:
            ax = ((sub + 2 * i) // 2)
            if ax in A:
                return [ax, i]
