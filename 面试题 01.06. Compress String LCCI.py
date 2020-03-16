class Solution:
    def compressString(self, S: str) -> str:
        # s = ''                    #这就是正常思维~
        # count = 1
        # for i in range(len(S)):
        #     if i == len(S)-1:s += '{}{}'.format(S[i], count)
        #     elif S[i] == S[i+1]:count += 1
        #     else:
        #         s += '{}{}'.format(S[i], count)
        #         count = 1
        # return s if len(s) < len(S) else S

        s = ''.join(c + str(len([*v])) for c, v in itertools.groupby(S))  #没想到itertools这么强大！里面竟然还有组合功能，还有笛卡尔积。噫，以后多学学。
        return len(s) < len(S) and s or S
