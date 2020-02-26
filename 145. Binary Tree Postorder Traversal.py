# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        #今天把三种遍历全部都用不同的方法实现了一遍，收获颇丰，其中这个后序遍历的第三种方法我没法简单的替换代码位置来实现，所以只有两种方法。好歹对得起它困难的模式~233
        if not root:return []
        nums = []

        # def helper(root):
        #     if root:
        #         helper(root.left)
        #         helper(root.right)
        #         nums.append(root.val)  
        # helper(root)
        # return nums

        stack = [(0, root)]
        while stack:
            flag, cur = stack.pop()
            if not flag:
                stack.append((1, cur))
                if cur.right:stack.append((0, cur.right))  # 这边的顺序还是要注意的，是反的
                if cur.left:stack.append((0, cur.left))
            else:
                nums.append(cur.val)
        return nums
