class Solution:
    def bitwiseComplement(self, N: int) -> int:
        # bin_n = bin(N)[2:]
        # ret = ''
        # for i in bin_n:
        #     if i == '0':
        #         ret += '1'
        #     else:
        #         ret += '0'
        # return int(ret, 2)

        if N == 0:
            return 1
        
        l = 0
        temp = N
        while N != 0:
            N >>= 1
            l += 1
        
        return 2**l - 1 - temp

        # return 1 if not N else N ^ int('1' * N.bit_length(), 2)
