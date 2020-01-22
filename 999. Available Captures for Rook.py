class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        stop = False
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    position = (i, j)
                    stop = True
                    break
            if stop:break
        def p_exists(rangee):
            for i in rangee:
                if i == 'B':
                    return 0
                if i == 'p':
                    return 1
            return 0
        i, j = position
        north = [row[j] for row in board[:i]][::-1]
        east = board[i][j:8]
        south = [row[j] for row in board[i:8]]
        west = board[i][:j][::-1]

        return p_exists(north) + p_exists(east) + p_exists(south) + p_exists(west)
