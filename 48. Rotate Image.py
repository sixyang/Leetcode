class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 我就很纳闷，为什么我的所有算法的提交时间都超过100ms？然后超过8%？emmmmm，同样的算法，差别也太大了吧。玄学。
        # matrix[:] = list(map(lambda x:x[::-1], zip(*matrix)))     这个就已经很慢了，100ms

        # import numpy as np                                        没想到这个更慢，152ms……
        # matrix[:] = np.rot90(matrix, -1)

        # ret = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        # for j in range(len(matrix)):
        #     for i in range(len(matrix[0])):
        #         ret[i][j] = matrix[j][len(matrix[0])-i-1]         这个我理解不来
        # matrix[:] = ret

        n = len(matrix)                                             #为啥这个花费时间还挺长？
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for k in range(n):
            matrix[k].reverse()               
