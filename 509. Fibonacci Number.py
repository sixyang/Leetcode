class Solution:
    def fib(self, N: int) -> int:
        # if N == 1 :return 1
        # elif N == 0:return 0
        # else:return self.fib(N-1) + self.fib(N-2)
        i0, i1 = 0, 1
        if N == 0:return 0
        if N == 1:return 1
        for i in range(N-1):
            i1, i0 = i0 + i1, i1
        return i1
                
