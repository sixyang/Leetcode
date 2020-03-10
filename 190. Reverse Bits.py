class Solution:
    def reverseBits(self, n: int) -> int:
        #之前做的时候没有注意到32位这个东西，所以出了问题。
        
        # bin_n = bin(n)[2:]
        # bin_n = ('0'*(32-n.bit_length())).join(['', bin_n])
        # return int(bin_n[::-1], 2)
        ret = 0
        for i in range(32):
            #这些二进制都挺玄乎的。
            m = n & 0x1
            n = n >> 1
            ret = ret + (m << (31 - i))
        return ret
