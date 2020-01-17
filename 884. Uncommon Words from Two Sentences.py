class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        list_a = A.split(' ')
        list_b = B.split(' ')
        from collections import Counter
        c_a = Counter(list_a)
        c_b = Counter(list_b)
        ret_a = self.once(list_a, list_b, c_a)
        ret_b = self.once(list_b, list_a, c_b)
        return ret_a + ret_b

    def once(self, list_a, list_b, c_a):
        ret = []
        set_b = set(list_b)
        for i in list_a:
            if i not in set_b and c_a[i] == 1:
                ret.append(i)
        return ret
