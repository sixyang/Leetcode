class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #这是第好几次做这个题目了，之前好像提交了，emmm，8次，都没过，这次想着用Counter来做的，然后过了，没想到Counter有这么多的方法啊。还能像集合那样交并集。太骚了。看来还得多多学习啊！
        from collections import Counter
        len1, len2 = len(nums1), len(nums2)
        c1, c2 = Counter(nums1), Counter(nums2)

        # ret = []                                  #这个是我一开始想到的方法。
        # if len1 < len2:
        #     for i in c1:
        #         if i in c2:
        #             lower = min(c1[i], c2[i])
        #             ret.extend([i]*lower)
        # else:
        #     for i in c2:
        #         if i in c1:
        #             lower = min(c1[i], c2[i])
        #             ret.extend([i]*lower)
        # return ret

        return list((c1 & c2).elements())
