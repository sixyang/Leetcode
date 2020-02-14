class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''代码看着感觉真丑，但是没办法啊，[] 这个测试案例搞了我好几次，哎，蓝廋。
            好歹最后还是做出来了，但是感觉二维数组最大的难点就是——麻烦，真的很麻烦。'''
        if len(matrix) == 0:return []
        if len(matrix) == 1:return matrix[0]

        n, m = len(matrix), len(matrix[0])
        
        i, j, ret = 0, 0, []
        status = 'right'
        while matrix[i][j] != '0':
            ret.append(matrix[i][j])
            if status == 'right':            
                if (j == m-1 or matrix[i][j+1] == '0'):
                    matrix[i][j] = '0'
                    i += 1
                    status = 'down'
                else:
                    matrix[i][j] = '0'
                    j += 1
            elif status == 'down':
                if (i == n-1 or matrix[i+1][j] == '0'):
                    matrix[i][j] = '0'
                    j -= 1
                    status = 'left'
                else:
                    matrix[i][j] = '0'
                    i += 1
            elif status == 'left':
                if (j == '0' or matrix[i][j-1] == '0'):
                    matrix[i][j] = '0'
                    i -= 1
                    status = 'up'
                else:
                    matrix[i][j] = '0'
                    j -= 1
            elif status == 'up':
                if (matrix[i-1][j] == '0'):
                    matrix[i][j] = '0'
                    j += 1
                    status = 'right'
                else:
                    matrix[i][j] = '0'
                    i -= 1
        return ret
