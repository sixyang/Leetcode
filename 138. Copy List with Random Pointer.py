"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # import copy
        # return copy.deepcopy(head)

        # r = ret = Node(0, None, None)         # 这是自己写的，感觉写的比较辣鸡
        # node = head
        # d = {}
        # index = 0
        # d2 = {}
        # while node:
        #     d[node] = index
        #     ret.next = temp = Node(node.val, None, None)
        #     if node.random:random_index = d.get(node.random)
        #     else:random_index = float('inf')
        #     if random_index != None and random_index < index:temp.random = d2[random_index]
        #     d2[index] = temp
        #     index += 1
        #     ret = ret.next
        #     node = node.next
        # node = head
        # ret = r.next
        # while node:
        #     if not ret.random and node.random:
        #         index = d.get(node.random)
        #         ret.random = d2.get(index)
        #     node = node.next
        #     ret = ret.next
        # return r.next

        def copyNode(node, res):
            # 果然链表用递归才是浪漫啊~
            if not node: return None
            if node in res: return res[node]
            copy = Node(node.val, None, None)
            res[node] = copy
            copy.next = copyNode(node.next, res)
            copy.random = copyNode(node.random, res)
            return copy

        return copyNode(head, {})
