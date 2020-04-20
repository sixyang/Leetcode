class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        ret = ''
        
        # 求A
        A = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
        ret += str(A) + 'A'

        # 求B
        sa = collections.Counter(secret)
        sb = collections.Counter(guess)
        B = 0
        cross = sa & sb
        for j in cross:
            B += cross[j]
        ret += str(B-A) + 'B'
        return ret
