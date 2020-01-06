class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ret = []
        
        from collections import Counter
        cnums = Counter(nums)
        for i in cnums.keys():
            if cnums[i] > 1:
                ret.append(i)
        
        nums_set = set(nums)
        snums = {i for i in range(1, len(nums)+1)}
        miss = snums - nums_set
        ret.extend(list(miss))
        return ret
