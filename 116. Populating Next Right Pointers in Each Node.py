"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # stack = collections.deque([root])         # 很显然，队列的bfs不满足题木要求，但是这个代码是是错的……
        # while stack:
        #     for i in range(len(stack)):
        #         node = stack.popleft()
        #         print(node.val, i)
        #         if i == len(stack)-1: node.next = None
        #         elif i < len(stack)-1: node.next = stack[0]
        #         if node.left: 
        #             stack.append(node.left)
        #         if node.right: 
        #             stack.append(node.right)
        # return root

        # if not root: return None                    # 这个是看了别人的解法后自己做出来的~虽然还是不懂~
        # if root.left: root.left.next = root.right
        # if root.right and root.next: root.right.next = root.next.left
        # self.connect(root.left)                     # 这里有点DFS的感觉，不是BFS
        # self.connect(root.right)
        # return root                                 # 我还是不理解这里return的root谁来接收~怎么连接起来的~

        if root:                                      # 这是typing monkey写的，太强了！
            l, r = root.left, root.right
            while l:
                l.next, l, r = r, l.right, r.left
            self.connect(root.left)
            self.connect(root.right)
            return root
