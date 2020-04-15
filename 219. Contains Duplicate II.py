class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):            # 暴力法果然没法AC……不过看着真的简单明了~
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j] and j - i <= k:return True
        # return False

        # counts = {}
        # for i in range(len(nums)):
        #     if nums[i] not in counts:
        #         counts[nums[i]] = [i]
        #     else:
        #         counts[nums[i]].append(i)
        # for j in counts:
        #     ele = counts[j]
        #     for m in range(1, len(ele)):
        #         if ele[m] - ele[m-1] <= k:return True
        # return False

        d={}                                    # 这别人写的代码真的棒！
        for i in range(len(nums)):
            if nums[i] in d and (i-d[nums[i]])<=k:
                return True
            d[nums[i]]=i
        return False
