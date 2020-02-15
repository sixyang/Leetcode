class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #写这道题目的时候竟然发现之前已经做过了。。但是看了一下之前拙略的代码，感觉好菜啊。哈哈哈，所以重新用排序，二分做了一遍，超过了84%，感觉还可以。
        #之前听别人说，如果你一年后不觉得一年之前的自己是个傻子，就说明你今年没什么进步，一年前正努力看《Python实践》那本书，现在已经在力扣上刷题了。过的好快。
        nums.sort()
        import bisect
        l = bisect.bisect_left(nums, val)
        r = bisect.bisect_right(nums, val)
        del nums[l: r]
