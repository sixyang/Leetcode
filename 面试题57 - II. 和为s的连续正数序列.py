class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        #感觉本质上是数学上的等差数组求和。然后解方程。
        n = target // 2 + 1
        ret = []
        while n > 0:
            delta = (2*n+1)**2-8*target
            if delta >= 0:
                m = (1 + delta**0.5)/2
                if int(m) == m:
                    m = int(m)
                    ret.append(list(range(m, n+1)))
            n -= 1
        return ret[::-1]
