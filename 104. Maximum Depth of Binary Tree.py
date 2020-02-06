# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0                 
        # left, right = 1, 1
        # if root.left:                                  #左右节点递归
        left = self.maxDepth(root.left)
        # if root.right:
        right = self.maxDepth(root.right)
        return max(left, right) + 1

        # while True:
        #     if root.left:
        #         left += 1
        #         root = root.left
        #     if root.right:
        #         right += 1
        #         root = root.right
        #     break
        # return max(left, right)
