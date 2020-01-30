class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # length = len(grid)-1              这边思路错了。
        # for i in range(length):
        #     width = len(grid[0])-1
        #     for j in range(width):
        #         if k < j:
        #             if j + k <= width:
        #                 grid[i][j], grid[i][j+k] = grid[i][j+k], grid[i][j]
        #             else:
        #                 if i < length:
        #                     m = i + 1
        #                 else:
        #                     m = 0
        #                 grid[i][j], grid[m][k-width-j] = grid[m][k-width-j], grid[i][j]
        # return grid
        temp, ret = [], []
        for i in grid:
            temp.extend(i)
        length = len(temp)
        if k > len(temp):
            k %= length    
        temp = temp[length-k:] + temp[:length-k]
        offset = len(grid[0])
        for i in range(len(grid)):
            ret.append(temp[i*offset: (i+1)*offset])   
        return ret
