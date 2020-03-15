class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        def infect(grid, i, j, area):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!= 1:return 0
            grid[i][j] = -1
            return 1 + infect(grid, i-1, j, area) + infect(grid, i+1, j, area) + infect(grid, i, j-1, area) + infect(grid, i, j+1, area)            #这一段是核心，之前的200题这边用的是分成四项，而计算数量要加起来！这个具体留作日后思考~

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    temp_area = infect(grid, i, j, 0)
                    area = max(area, temp_area)
        return area
                    
        
