# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # 这种套模板的题目是真的爽啊！不过没想到的是竟然还有负数，搞得我还得把max_val初始值设为 -float('inf')
        if not root: return []
        queue = collections.deque([root])
        ret = []
        while queue:
            max_val = -float('inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.val > max_val: max_val = node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ret.append(max_val)
        return ret
