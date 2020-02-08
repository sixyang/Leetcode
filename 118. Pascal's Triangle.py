class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nums = [[0 for j in range(i+1)] for i in range(numRows)]

        # for i in range(numRows):
        #     m = i
        #     n = 1
        #     while n < m:
        #         if n != m:
        #             nums[m][n] = nums[m-1][n-1] + nums[m-1][n]       
        #         n += 1
        # return nums
        
        def recursion(i, j):
            if j == 0 or j == i:
                return 1
            if nums[i][j] != 0:
                return nums[i][j]
            return recursion(i-1, j-1) + recursion(i-1, j)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] == 0:
                    nums[i][j] = recursion(i, j)
        return nums 
