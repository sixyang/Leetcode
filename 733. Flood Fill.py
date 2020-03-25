class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # 唔啊，看着都觉得麻烦，感觉还是用递归比较好~明天琢磨着弄个递归吧
        length, width = len(image), len(image[0])
        val = image[sr][sc]
        stack = [(sr, sc)]
        image[sr][sc] = newColor
        visited = set()
        while stack:
            middle = stack.pop()
            left = (middle[0], middle[1]-1)
            right = (middle[0], middle[1]+1)
            up = (middle[0]-1, middle[1])
            down = (middle[0]+1, middle[1])
            if left[1]>=0 and image[left[0]][left[1]] == val and left not in visited:
                visited.add(left)
                image[left[0]][left[1]] = newColor
                stack.append(left)
            if right[1]<width and image[right[0]][right[1]] == val and right not in visited:
                visited.add(right)
                image[right[0]][right[1]] = newColor
                stack.append(right)
            if up[0]>=0 and image[up[0]][up[1]] == val and up not in visited:
                visited.add(up)
                image[up[0]][up[1]] = newColor
                stack.append(up)
            if down[0]<length and image[down[0]][down[1]] == val and down not in visited:
                visited.add(down)
                image[down[0]][down[1]] = newColor
                stack.append(down)
        return image                                            
