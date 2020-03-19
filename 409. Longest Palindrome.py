class Solution:
    def longestPalindrome(self, s: str) -> int:
        # emmm，这也太简单了吧，按照思路来写就好了~
        from collections import Counter
        count = Counter(s)
        ret = 0
        flag = False
        for i in count:
            if count[i] % 2 == 0:
                ret += count[i]
            elif count[i] > 1 and count[i] % 2 == 1:
                ret += count[i]-1
                flag = True
            else:flag = True
        if flag:ret += 1
        return ret
