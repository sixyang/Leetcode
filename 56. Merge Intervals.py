class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ''' 这是2020.4.16的每日一题，一开始看着挺简单的，但是前后做了有2个半小时，emmm，有点上头，这或许就是刷题的快乐吧，本来是想放弃的，但是最终还是咬着牙清空代码重新整理思路写了一遍。确实，做题最重要的就是清晰的头脑，一定要在纸上将题目核心代码写一遍，并且手动debug，这样思路才会清晰，遇到麻烦的题目也不会怂。
        唉，就这么不到20行代码，搞了2个半小时，果真是 一杯茶，一包烟，一道题目做半天😑'''
        if len(intervals) <= 1:return intervals
        ret = []
        intervals = sorted(intervals, key=lambda x:x[0])
        ind, length = 1, len(intervals)
        left = intervals[ind-1]
        while ind < length:
            right = intervals[ind]
            if left[1] >= right[0]:
                if left[1] < right[1]:
                    left = [left[0], right[1]]
                if ind == length-1:ret.append(left)
            else:
                if left not in ret:ret.append(left)
                if ind == length-1:ret.append(right)
                left = intervals[ind]
            ind += 1
        if right[0] > left[1]:ret.append(right)
        return ret
