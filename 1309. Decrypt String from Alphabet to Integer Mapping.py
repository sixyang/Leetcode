class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret, dic = '', {}              
        for i in range(1, 27):
            if i < 10:
                dic[str(i)] = chr(96+i)
            else:
                dic[str(i)+'#'] = chr(96+i)

        # index = 0                             突然想起来，为什么不能逆序遍历呢，，就不要考虑加2了。
        # while index < len(s)-2:
        #     if s[index+2] != '#':
        #         ret += dic[s[index]]
        #     else:
        #         ret += dic[s[index: index+3]]
        #         index += 3
        #         continue
        #     index += 1
        # length = len(s)
        # if index != length:
        #     for i in reversed(range(length-index)):
        #         ret += dic[s[-i-1]]
        # return ret
        index = len(s) - 1
        while index >= 0:
            if s[index] == '#':
                ret += dic[s[index-2: index+1]]
                index -= 3
            else:
                ret += dic[s[index]]
                index -= 1
        return ret[::-1]
