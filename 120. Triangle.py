class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        bottom = len(triangle)-1
        width = len(triangle[-1])
        # def recursion(i, j, total):
        #     total += triangle[i][j]
        #     if i == bottom:   
        #         return total
        #     else:
        #         left = recursion(i+1, j, total)
        #         right = recursion(i+1, j+1, total)
        #         return min(left, right)
        # return recursion(0, 0, 0)
        
        dp = [[0 for i in range(j+1)] for j in range(len(triangle))]
        # def recursion(m, n):
        #     if m >= bottom or n >= width:return 0
        #     if grid[m][n] != 0:return grid[m][n]
        #     grid[m][n] =  min(recursion(m+1, n), recursion(m+1, n+1)) + triangle[m][n]
        #     return grid[m][n]
        # return recursion(0, 0)

        # def rec(i, j):
        #     if i == 0 or j == 0:return triangle[i][j]
        #     if i < 0:return 0

        #     dp[i][j] = min(dp[i-1][j-1] + dp[i-1][j]) + triangle[i][j]
        #     return dp[i][j]
        # return rec(len(dp), len(dp[-1]))

        # if not triangle: return 0
        # res = triangle[-1]
        # for i in xrange(len(triangle)-2, -1, -1):
        #     for j in xrange(len(triangle[i])):
        #         res[j] = min(res[j], res[j+1]) + triangle[i][j]
        # return res[0]
        if len(triangle) == 0:return 0
        if len(triangle) == 1:return triangle[0][0]
        dp[0][0] = triangle[0][0]
        dp[1][0] = triangle[0][0] + triangle[1][0]
        dp[1][1] = triangle[0][0] + triangle[1][1]
        for idx1, ele1 in enumerate(triangle):
            for idx2, ele2 in enumerate(ele1):
                if idx1 > 1:
                    if idx1 > idx2 >= 1:
                        dp[idx1][idx2] = min(dp[idx1-1][idx2-1], dp[idx1-1][idx2]) + triangle[idx1][idx2]
                    elif idx2 == 0:
                        dp[idx1][idx2] = dp[idx1-1][idx2] + triangle[idx1][idx2]
                    else:
                        dp[idx1][idx2] = dp[idx1-1][idx2-1] + triangle[idx1][idx2]
        return min(dp[-1])
