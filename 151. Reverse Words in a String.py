class Solution:
    def reverseWords(self, s: str) -> str:
        #这道题目显示为中等难度，但是如果用函数的话就是非常简单的题目。。emmm，关于用库我觉得还是得辩证地看待。看实际情况吧。
        words = s.split(' ')
        temp = []
        for i in range(len(words)):
            if words[i] != '':
                temp.append(words[i])
        return ' '.join(temp[::-1])
