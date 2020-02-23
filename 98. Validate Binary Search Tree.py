# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # lst = []
    def isValidBST(self, root: TreeNode) -> bool:
        # if not root:return True                   这个只能确认父子关系，没法确认爷孙
        # if root.left:
        #     if root.left.val < root.val:
        #         self.lst.append(root.left.val)
        #         l = self.isValidBST(root.left)
        #     else:return False
        # if root.right:
        #     if root.right.val > root.val:
        #         self.lst.append(root.right.val)
        #         r = self.isValidBST(root.right) 
        #     else:return False
        # print(self.lst)
        # return True

        lst = []                                    #果然还是中序遍历靠谱。                    
        def helper(root):
            if root:                                #这边条件不能错~
                helper(root.left)
                lst.append(root.val)
                helper(root.right)
        helper(root)
        return sorted(lst) == lst and len(set(lst)) == len(lst)
