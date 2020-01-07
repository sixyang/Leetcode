class Solution:
    def toLowerCase(self, string: str) -> str:
        # return string.lower()
        s = ''
        for i in string:
            if 65 <= ord(i) <= 90:
                s += chr(ord(i) + 32)
            else:
                s += i
        return s
