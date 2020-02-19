class Solution:
    def reverseWords(self, s: str) -> str:
        #也许用库是一件不好的事情，？但是它实在是太香了~
        l = s.split(' ')
        t = []
        for i in l:
            if i != '':
                t.append(i)
        temp = map(lambda x:x[::-1], t)
        return ' '.join(temp)
        
