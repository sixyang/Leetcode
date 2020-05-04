# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 因为是二叉搜索树，所以很容易定位到值，然后记录定位的路径，生成两个数组，寻找两个数组第一个不相同的值~
        # def findval(root1, node):
        #     root = root1
        #     track = []
        #     while root.val != node.val:
        #         track.append(root)
        #         if root.val > node.val:
        #             root = root.left
        #         elif root.val < node.val:
        #             root = root.right
        #     track.append(root)
        #     return track
        # pt = findval(root, p)
        # qt = findval(root, q)
        # min_track = len(pt) if len(pt) < len(qt) else len(qt)
        # # 我在这儿卡了好长时间，这里本质就是寻找两个数组第一个不相同的值，但是愣是好久没做出来……
        # for i in range(min_track):
        #     if qt[i] != pt[i]:
        #         return qt[i-1]
        # return qt[i]

        # 艹，我想到了利用二叉搜索树，但是没想到性质能用的这么骚~看来我只是在第一层……/(ㄒoㄒ)/~~
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
        # 如果两个值同大于根值，则最大公共祖先一定在right，否则一定在left，如果两个值分别在左右，就说明此时的值就是最近公共祖先！牛逼，这算法~
