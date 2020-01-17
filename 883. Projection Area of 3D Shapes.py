class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        from numpy import array, sum, max
        grid = array(grid)
        bottom = sum(grid > 0)
        side = sum(max(grid, axis=1))
        front = sum(max(grid, axis=0))
        return int(bottom + side + front)
