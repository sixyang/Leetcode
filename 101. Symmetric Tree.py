# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # if root:                              #这个代码是错的！
        #     if all([root.left, root.right]):
        #         a = self.isSymmetric(root.left)
        #         b = self.isSymmetric(root.right)
        #         return a * b
        #     else:
        #         return False
        # else:return True

        if not root:return True
        from collections import deque
        queue = deque()
        node = root
        
        queue.append(node)
        while queue:                            #记忆中的BFS，看来，光记模板是没什么用的，根据题目改进模板非常重要！
        ret = []
            length = len(queue)
            for i in range(length):
                pNode = queue.popleft()
                if pNode.left:
                    queue.append(pNode.left)
                    ret.append(pNode.left.val)
                else:ret.append(None)
                if pNode.right:
                    queue.append(pNode.right)
                    ret.append(pNode.right.val)
                else:
                    ret.append(None)
            if ret[::-1] != ret:return False
        return True
