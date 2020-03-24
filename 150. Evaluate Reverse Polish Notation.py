class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #挺简单的，按照思路来写就好了~我印象里逆波兰表达式比这个要复杂很多，还有括号来着……
        stack = []
        operations = {'+', '-', '*', '/'}
        for i in tokens:
            if i in operations:
                c1 = int(stack.pop())
                c2 = int(stack.pop())
                if i == '+':r = c1 + c2
                elif i == '-':r = c2 - c1
                elif i == '*':r = c2 * c1
                elif i == '/':r = int(c2 / c1)
                stack.append(r)
            else:
                stack.append(i)
        return int(stack[-1])
