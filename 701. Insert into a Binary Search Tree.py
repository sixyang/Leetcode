# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 艹，时间复杂度超过15%，emmm，怎么这么慢的，但是空间复杂度超过100%~  ブ(*￣▽￣*)ブ
        # if not root: return TreeNode(val) 
        # node = root
        # while node and (node.left or node.right):   # 这里要先判断node
        #     if node.val < val and node.right:       # 这里要注意node.right不存在的情况，不然会出错！
        #         node = node.right
        #     elif node.val > val and node.left:
        #         node = node.left
        #     else: break
        # if node.val > val: node.left = TreeNode(val)
        # else: node.right = TreeNode(val)
        # return root

        if not root: return TreeNode(val)              # 这递归就真的是玄学~
        if root.val < val: root.right = self.insertIntoBST(root.right, val)
        else: root.left = self.insertIntoBST(root.left, val)
        return root
