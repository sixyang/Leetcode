# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #现在已经挺熟悉的了，直接手写层序遍历，o(*￣▽￣*)ブ
        if not root:return []
        from collections import deque
        queue = deque()
        node = root
        queue.append(root)
        ret = []
        while queue:
            temp = []
            for _ in range(len(queue)):
                pNode = queue.popleft()
                temp.append(pNode.val)
                if pNode.left:queue.append(pNode.left)
                if pNode.right:queue.append(pNode.right)
            ret.append(temp)
        return ret
