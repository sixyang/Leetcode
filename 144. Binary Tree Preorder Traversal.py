# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #DFS还真的是万能啊！各种遍历改个顺序就好了~
        if not root:return []
        nums = []
        stack = [(0, root)]
        while stack:
            flag, cur = stack.pop()
            if not flag:
                if cur.right:stack.append((0, cur.right))        #这边的顺序还是要注意的，是反的
                if cur.left:stack.append((0, cur.left))
                stack.append((1, cur))
            else:
                nums.append(cur.val)
        return nums
