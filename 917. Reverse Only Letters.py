class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        temp = []
        ret = []
        # for i in S:
        #     if 97 <= ord(i) <= 122 or 65 <= ord(i) <= 90:
        #         temp.append(i)
        # temp = temp[::-1]
        # index = 0
        # for e in S:
        #     if 97 <= ord(e) <= 122 or 65 <= ord(e) <= 90:
        #         ret.append(temp[index])
        #         index += 1
        #     else:
        #         ret.append(e)
        # return ''.join(ret)
        s = S[::-1]
        index = -1
        for i in S:
            if 97 <= ord(i) <= 122 or 65 <= ord(i) <= 90:
                while True:
                    if 97 <= ord(S[index]) <= 122 or 65 <= ord(S[index]) <= 90:
                        ret.append(S[index])
                        index -= 1
                        break
                    index -= 1
            else:
                ret.append(i)
        return ''.join(ret)
