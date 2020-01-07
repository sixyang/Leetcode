class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:return True
        li_s = list(s)
        left = 0
        right = len(s) - 1
        while left <= right:
            if li_s[left] == li_s[right]:
                left += 1
                right -= 1
            else:
                temp1 = li_s[left: right]
                temp2 = li_s[left + 1: right + 1]
                return temp1 == temp1[::-1] or temp2 == temp2[::-1]
