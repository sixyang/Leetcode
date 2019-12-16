class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = sorted(s, key=lambda y: ord(y))
        # t = sorted(t, key=lambda x: ord(x))
        # return s == t
        return sorted(s) == sorted(t)
