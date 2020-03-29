class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # ret = [[0 for __ in range(len(matrix[0]))]for _ in range(len(matrix))]
        # def bfs(matrix, i, j):
        #     queue = collections.deque([(i, j)])
        #     nei = 0
        #     m, n = len(matrix), len(matrix[0])
        #     visited = set()
        #     while queue:
        #         nei += 1
        #         for k in range(len(queue)):
        #             p = queue.popleft()
        #             if p not in visited:
        #                 visited.add(p)
        #             if p[0]-1>=0:
        #                 if matrix[p[0]-1][p[1]] == 0:return nei
        #                 else:queue.append((p[0]-1,p[1]))
        #             if p[0]+1<m:
        #                 if matrix[p[0]+1][p[1]] == 0:return nei
        #                 else:queue.append((p[0]+1,p[1]))
        #             if p[1]-1>=0:
        #                 if matrix[p[0]][p[1]-1] == 0:return nei
        #                 else:queue.append((p[0],p[1]-1))
        #             if p[1]+1<n:
        #                 if matrix[p[0]][p[1]+1] == 0:return nei
        #                 else:queue.append((p[0],p[1]+1))
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:ret[i][j] = 0
        #         else:
        #             ret[i][j] = bfs(matrix, i, j)
        # return ret

        # 矩阵的BFS，先找出所有0点，然后围绕每个0点进行bfs展开，这样周围的1点就能获得最近0点的距离~
        m, n = len(matrix), len(matrix[0])
        queue = collections.deque()
        visited = set()
        for i in range(m):              # 将所有0点加入队列和visited
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        while queue:
            i, j = queue.popleft()      # 这里用i，j避免下面复杂的表示~
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:   # 这一步真的是妙🌞
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    matrix[x][y] = matrix[i][j] + 1                 # 这就是在蔓延~
                    visited.add((x, y))
                    queue.append((x, y))
        return matrix
