class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 不会位运算的我，只能用这种方法了~
        # counter = collections.Counter(nums)
        # ret = []
        # for i in counter:
        #     if counter[i] == 1: ret.append(i)
        # return ret

        ret, index = 0, 0
        for n in nums:
            ret ^= n
        # 找从右向左数第几位不同，也就是第index位
        # 这一步其实可以根据n & (-n)的快捷方式获得，不过对位运算掌握不是那么熟练的话，记结论容易忘，不如理解实质
        while ret & 1 == 0:
            index += 1
            ret >>= 1
        r1, r2 = 0, 0
        for n in nums:
            if (n >> index) & 1 == 0:
                r1 ^= n
            else:
                r2 ^= n
        return [r1, r2]
