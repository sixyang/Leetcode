class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 哈哈，当初感觉这道题目肯定很难，现在做来感觉还是挺简单的，只要按照想法敲就好了。就是花费的内存有点多。QWQ 而且这代码看着挺难受的。以后再来优化吧。:)
        length = len(board)
        for i in range(length):
            row = set()
            for j in range(length):
                if board[i][j] != '.':
                    if board[i][j] not in row:row.add(board[i][j])
                    else:return False

        for x in [1, 4, 7]:
            for y in [1, 4, 7]:
                square = set()
                for k in [x-1, x, x+1]:
                    for b in [y-1, y, y+1]:
                        if board[k][b] != '.':
                            if board[k][b] not in square:square.add(board[k][b])
                            else:return False

        for m in range(length):
            for n in range(m, length):
                board[m][n], board[n][m] = board[n][m], board[m][n]
        for m in range(length):
            column = set()
            for n in range(length):
                if board[m][n] != '.':
                    if board[m][n] not in column:column.add(board[m][n])
                    else:return False
        return True
