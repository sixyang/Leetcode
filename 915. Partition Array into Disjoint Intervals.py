class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        '''思路就是：先找出最小值，要求的索引肯定在最小值右边。然后比较左边的最大值l和右边的最小值r，直到r >= l为止。思路还是非常清晰地，但是代码写起来还是比较麻烦。'''
        def find_min(nums):
            '''返回nums里最小的数的索引'''
            min_val = 10**6
            min_ind = 0
            for i in range(len(nums)):
                if nums[i] < min_val:
                    min_ind = i
                    min_val = nums[i]
            return min_ind
        def find_max(nums):
            '''返回nums里最大的数的索引'''
            max_val = 0
            max_ind = 0
            for i in range(len(nums)):
                if nums[i] > max_val:
                    max_ind = i
                    max_val = nums[i]
            return max_ind
            
        min_ind = find_min(A)
        left_min_ind = find_max(A[: min_ind])
        right_min_ind = find_min(A[min_ind+1: ]) + min_ind + 1
        while right_min_ind < len(A):
            if A[right_min_ind] >= A[left_min_ind]:
                return min_ind + 1
            else:
                left_min_ind = find_max(A[: right_min_ind])
                min_ind = right_min_ind
                right_min_ind = find_min(A[right_min_ind+1: ]) + right_min_ind+1
