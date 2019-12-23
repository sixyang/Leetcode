class Solution:
    def reverseVowels(self, s: str) -> str:
        # simple = 'AEIOUaeiou'
        # temp = []
        # length = len(s)
        # li_s = list(s)
        # for i in range(length):
        #     if li_s[i] in simple:
        #         temp.append(li_s[i])
        #         li_s[i] = '~'
        # for i in range(length):
        #     if li_s[i] == '~' and temp:
        #         li_s[i] = temp.pop()
        # return ''.join(li_s)
        simple = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left, right = 0, len(s) - 1
        li, temp = list(s), []
        while left <= right:
            if li[left] in simple:
                while True:
                    if li[right] in simple:
                        li[left], li[right] = li[right], li[left]
                        right -= 1
                        left += 1
                        break
                    else:
                        right -= 1
            else:

                if li[right] in simple:
                    left += 1
                else:
                    left += 1
                    right -= 1
        return ''.join(li)
