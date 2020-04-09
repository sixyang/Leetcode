class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # length, width = len(image), len(image[0])
        # val = image[sr][sc]
        # stack = [(sr, sc)]
        # image[sr][sc] = newColor
        # visited = set()
        # while stack:
        #     middle = stack.pop()
        #     left = (middle[0], middle[1]-1)
        #     right = (middle[0], middle[1]+1)
        #     up = (middle[0]-1, middle[1])
        #     down = (middle[0]+1, middle[1])
        #     if left[1]>=0 and image[left[0]][left[1]] == val and left not in visited:
        #         visited.add(left)
        #         image[left[0]][left[1]] = newColor
        #         stack.append(left)
        #     if right[1]<width and image[right[0]][right[1]] == val and right not in visited:
        #         visited.add(right)
        #         image[right[0]][right[1]] = newColor
        #         stack.append(right)
        #     if up[0]>=0 and image[up[0]][up[1]] == val and up not in visited:
        #         visited.add(up)
        #         image[up[0]][up[1]] = newColor
        #         stack.append(up)
        #     if down[0]<length and image[down[0]][down[1]] == val and down not in visited:
        #         visited.add(down)
        #         image[down[0]][down[1]] = newColor
        #         stack.append(down)
        # return image

        # 这代码看着真舒服~
        m, n = len(image), len(image[0])
        stack = [(sr, sc)]
        color = image[sr][sc]
        visited = set([(sr, sc)])
        while stack:
            i, j = stack.pop()      # 要点一：这里用i, j比元组p方便多了~
            image[i][j] = newColor  # 要点二：可以在这里进行操作，会针对每个点，就没必要将初始点特殊处理
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]: # 要点三：这个神奇的列表，清晰方便
                if 0<= x < m and 0<= y < n and image[x][y] == color and (x, y) not in visited:
                    # 要点四：这四个条件不能少，别忘了visited判断！
                    visited.add((x, y))
                    stack.append((x, y))
        return image
