class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Game of life.  游戏人生？😂既然不能边看周围情况边更改元素，那就弄个列表，把要改的index记下来，等情况看完了再修改就好了
        live_points = []
        dead_points = []
        def surround(board, i, j):
            live_nums = 0
            for k in [i-1, i, i+1]:
                for m in [j-1, j, j+1]:
                    if k >= 0 and m >= 0 and k < len(board) and m < len(board[0]):
                        if board[k][m] == 1:live_nums += 1
            return live_nums
        for i in range(len(board)):
            for j in range(len(board[0])):
                live_nums = surround(board, i, j)
                if board[i][j] == 0:
                    if live_nums == 3:live_points.append((i, j))
                else:
                    live_nums -= 1
                    if live_nums < 2 or live_nums > 3:dead_points.append((i, j))
        for pl1, pl2 in live_points:board[pl1][pl2] = 1
        for pd1, pd2 in dead_points:board[pd1][pd2] = 0
