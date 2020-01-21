class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        # from collections import Counter
        # a = Counter(A)
        # length = len(A)
        # for ele, value in a.items():
        #     if value >= length // 2:
        #         return ele

        a = set()
        for i in A:
            if i in a:
                return i
            else:
                a.add(i)
