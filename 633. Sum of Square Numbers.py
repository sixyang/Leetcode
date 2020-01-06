class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # half = c ** 0.5
        # if int(half) == half:return True
        # half = int(half)
        # while half >= 0:
        #     b = (c - half ** 2) ** 0.5
        #     if int(b) == b:
        #         return True
        #     else:
        #         half -= 1
        # return False
        if c <= 2:
            return True
        while c % 2 == 0:
            c = c // 2
        p = 3
        while p * p <= c:
            index = 0
            while c % p == 0:
                index += 1
                c = c // p
            if (p % 4 == 3) and (index % 2 == 1):
                return False
            p += 2
        return c % 4 == 1

        '''
        解释下Python3最高记录的非双指针解法。 看上去会让人很费解，但是只要知道定理就很好理解了。

        if c <= 2:
            return True
        while c % 2 == 0:
            c = c // 2
        p = 3
        while p * p <= c:
            index = 0
            while c % p == 0:
                index += 1
                c = c // p
            if (p % 4 == 3) and (index % 2 == 1):
                return False
            p += 2
        return c % 4 == 1
定理：某个正整数是两平方数之和，当且仅当该正整数的所有 4k+3 型素因数的幂次均为偶数。 任何一个正整数都可以因数分解为 c = (2^r)*(p1^n1)*(p2^n2)*...*(pk^nk)，其中p1...pk为素因数，n1...nk为因数的幂次。 也就是说有一个形如4k+3的素因数pi，如果ni为奇数，那它就不可能被写为两个整数的平方数之和了。

代码第一步就是将2全部去掉，做素因数分解。

        if c <= 2:
            return True
        while c % 2 == 0:
            c = c // 2
做因数分解的同时，判断素因数的类型和幂次。

        p = 3
        while p * p <= c:
            index = 0
            while c % p == 0:
                index += 1
                c = c // p
            if (p % 4 == 3) and (index % 2 == 1):
                return False
            p += 2
分解到最后的c实际上是一个素数，这时候其实判断c是形如4k+1的素数，那肯定可以写为两整数平方和（也可以判断不是形如4k+3的素数也行）

return c % 4 == 1 # 或者 c % 4 != 3
        '''
