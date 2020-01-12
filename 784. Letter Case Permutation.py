class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ret = []
        for i in S:
            if i.isalpha():
                if not ret:
                    ret.extend([i.lower(), i.upper()])
                else:
                    ret1, ret2 = ret.copy(), ret.copy()
                    for j in range(len(ret1)):
                        ret1[j] += i.lower()
                    for k in range(len(ret2)):
                        ret2[k] += i.upper()
                    ret = ret1 + ret2
            else:
                if ret:
                    for m in range(len(ret)):
                        ret[m] += i
                else:
                    ret.extend([i])
        return ret
