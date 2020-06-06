class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # 执行用时 : 6128 ms, 在所有 Python3 提交中击败了 5.05%的用户; 内存消耗 : 15 MB, 在所有 Python3 提交中击败了 6.25%的用户. 哈哈，太惨了……
        count = collections.Counter(nums)
        most = count.most_common()
        most_val = most[0][1]
        most_vals = []
        for i in most:
            if i[1] == most_val: most_vals.append(i[0])
            else: break
        
        least = float('inf')
        for j in most_vals:
            l, r = 0, len(nums)-1
            while l < r:
                if nums[l] != j: l += 1
                if nums[r] != j: r -= 1
                if nums[l] == j and nums[r] == j: break
            if r-l+1 < least: least = r-l+1
        return least
                    
            
