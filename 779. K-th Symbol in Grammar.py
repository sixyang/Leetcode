class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        # ret, index = '0', 1               #这个方法中间有很多的多余项，将所有的东西都计算出来，费劲。
        # while index <= N:
        #     result = ''
        #     for i in ret:
        #         result += '01' if i == '0' else '10'
        #     index += 1
        #     ret = result
        # return ret[K-1]

        # def recursion(k):                 #这是我的失败品。
        #     if k == 0:return 0
        #     if k == 1:return 1
        #     k = k//2 if k % 2 == 0 else (k//2+1)
        #     return recursion(k)
        # ret = recursion(K)
        # b=-(ret-1)
        # return ret if K % 2 == 1 else b

        if K == 1:return 0
        ret = self.kthGrammar(N-1, (K+1)//2)
        return ret if K % 2 == 1 else -(ret-1)
