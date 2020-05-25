# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = collections.deque([root])
        # nums = []                                 # 自己写的算法好丑啊
        # index = 0
        # while queue:
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left: 
        #             index += 1
        #             queue.append(node.left)
        #             nums.append(node.left.val)
        #         else: nums.append('null')
        #         if node.right: 
        #             index += 1
        #             queue.append(node.right)
        #             nums.append(node.right.val)
        #         else: nums.append('null')
        # for i in range(index):
        #     if nums[i] == 'null': return False
        # return True

        while True:
            node = queue.popleft()
            if not node: break
            queue.append(node.left)             # 根本不需要判断left right存不存在，直接添加就好了
            queue.append(node.right)
        while queue:
            if queue.popleft(): return False
        return True
                
