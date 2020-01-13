class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        list_s = self.recursion(S)
        list_t = self.recursion(T)
        return list_s == list_t

    def recursion(self, S):
        list_s = []
        for i in S:
            if i == '#' and list_s:
                list_s.pop()
            elif i != '#':
                list_s.append(i)
        return list_s
