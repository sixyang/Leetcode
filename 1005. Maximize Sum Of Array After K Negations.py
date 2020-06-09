class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        # 先将列表排个序，然后看K和neg_count大小，如果K大，就说明能够充分的将所有的负数全部转变为正数，然后如果剩下的K为偶，就说明没有多余的转变，否则就要将 减去 2 * min，注意：这里是 2 *！！
        # 然后如果neg_count大，就从后往前遍历，将绝对值大的元素转变成正数，直到K的次数用完~
        # 难度 ： ⭐
        ret = 0
        nums = sorted(A, key=abs)
        neg_count = 0
        for i in nums:
            if i < 0: neg_count += 1
        if K >= neg_count:
            for j in nums:
                ret += abs(j)
            K -= neg_count
            if K % 2 == 0: return ret
            return ret - 2*abs(nums[0])
        else:
            index = len(nums)-1
            while index >= 0:
                if K > 0: ret += abs(nums[index])
                else: ret += nums[index]
                if nums[index] < 0: K -= 1
                index -= 1
            return ret
                
