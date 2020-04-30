class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 直接按照思路来写还是挺简单的，但是这个复杂度比较高，看评论说可以只记录首行和首列，然后再置零~
        position = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0: position.append((i, j))
        ret = set()
        for p in position:
            for i in range(len(matrix)):
                ret.add((i, p[1]))
            for j in range(len(matrix[0])):
                ret.add((p[0], j))
        for x, y in ret:
            matrix[x][y] = 0
