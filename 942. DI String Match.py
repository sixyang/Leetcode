class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        # 为什么相同的代码我要慢好多……
        l, r = 0, len(S)
        index = 0
        ret = []
        while l < r:
            if S[index] == 'I':
                ret.append(l)
                l += 1
            else:
                ret.append(r)
                r -= 1
            index += 1
        ret.append(l)
        return ret
