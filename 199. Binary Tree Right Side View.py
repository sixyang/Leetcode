# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # 今天的题目太简单了吧(￣▽￣)"，5分钟做完，一次性过~ 同时，Python3这里的类型标注真的是太有用了，不然都不知道应该返回什么类型~
        if not root: return []
        queue = collections.deque([root])
        ret = []
        while queue:
            ret.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return ret
                
