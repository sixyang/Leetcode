# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # stack, ret = [], []
        # pNode = root
        # while pNode or stack:
        #     if pNode:
        #         stack.append(pNode)
        #         pNode = pNode.left
        #     else:
        #         node = stack.pop()
        #         ret.append(node.val)
        #         pNode = node.right
        # return ret

        # ret = []
        # def inorder(root):
        #     if root:
        #         inorder(root.left)
        #         ret.append(root.val)
        #         inorder(root.right)
        # inorder(root)
        # return ret

        if not root:return []
        nums = []
        stack = [(0, root)]
        while stack:
            flag, cur = stack.pop()
            if not flag:
                if cur.right:stack.append((0, cur.right))        #这边的顺序还是要注意的，是反的
                stack.append((1, cur))
                if cur.left:stack.append((0, cur.left))
            else:
                nums.append(cur.val)
        return nums
