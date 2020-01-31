class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product, nsum, temp_num = 1, 0, n
        # for i in xrange(len(str(n))):           #注意，这里用了temp_num, 下面所有相关的运算都要用temp_num
        #     last_num = temp_num % 10
        #     temp_num //= 10
        #     product *= last_num
        #     nsum += last_num
        # return product - nsum

        for i in str(n):
            product *= int(i) 
            nsum += int(i)
        return product - nsum
