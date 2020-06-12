# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        # 其实这里可以不用self.q 和 self.p，那就需要在递归里面多加一个参数了。
        self.p = []
        self.q = []
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pp = qq = []
        def track(node, t):
            # 记录到某个节点的路径，为一个列表
            if node: 
                t.append(node)
                if node.left or node.right:
                    track(node.left, t)
                    track(node.right, t)
                if node.val == p.val: self.p = t.copy()
                if node.val == q.val: self.q = t.copy()
                t.pop()
        track(root, [])

        min_len = len(self.p) if len(self.p) < len(self.q) else len(self.q)
        for i in range(min_len):            # 遍历两个列表，遇到第一个不同元素 或 小列表到底了即返回值
            if self.p[i].val != self.q[i].val:
                return self.p[i-1]
            if i == min_len-1: 
                return self.p[i]
        
