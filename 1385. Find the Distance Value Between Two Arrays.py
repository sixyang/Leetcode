class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # 这道题目只有 6个赞~ 太惨了~
        ret = 0
        for i in arr1:
            if all([abs(i-j)>d for j in arr2]): ret += 1
        return ret
