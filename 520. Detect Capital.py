class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first = word[0]
        if 65 <= ord(first) <= 90:
            lower = False
            upper = False
            for i in range(1, len(word)):
                if 65 <= ord(word[i]) <= 90:
                    if lower:
                        return False
                    else:
                        upper = True
                elif 97 <= ord(word[i]) <= 122:
                    if upper:
                        return False
                    else:
                        lower = True
            return True
        elif 97 <= ord(first) <= 122:
            for i in range(1, len(word)):
                if 65 <= ord(word[i]) <= 90:
                    return False
            return True
