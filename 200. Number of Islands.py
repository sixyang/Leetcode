class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #这道题目我也想到了用这种蔓延的方法，但是我的纠结点是在确定完一个岛之后怎么看下一个岛，用 in ？那样复杂度太高了，没想到直接可以用循环。emmmm，突然脑抽。emmm
        #同时，我没想到怎么蔓延，因为我的方式里只有蔓延一次上下左右四个地方，所以不完全。没想到用递归，噫，所以递归真的太强大了。
        def infect(grid, i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':return
            grid[i][j] = '-1'
            infect(grid, i-1, j)            #注意，这里是个递归！我一开始还没发现……
            infect(grid, i+1, j)
            infect(grid, i, j+1)
            infect(grid, i, j-1)
        island_nums = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    infect(grid, i, j)
                    island_nums += 1
        return island_nums
