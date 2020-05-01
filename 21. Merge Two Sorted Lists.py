# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if not l1 and l2: return l2       # cao，没看清题目，竟然是有序的 Σ(っ °Д °;)っ
        # dummy = l1
        # while l1 and l2:
        #     next1 = l1.next
        #     l1.next = l2
        #     l1 = next1
        #     next2 = l2.next
        #     l2.next = next1
        #     prev = l2
        #     l2 = next2
        # if l2:
        #     prev.next = next2
        # return dummy

        # if not l1: return l2              # 这个递归太骚了，学不来学不来~
        # if not l2: return l1
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2

        ret = ListNode(None)                # 这个代码很棒！
        node = ret
        while l1 and l2:
            if l1.val <= l2.val:
                node.next, l1 = l1, l1.next
            else:
                node.next, l2 = l2, l2.next
            node = node.next
        if l1: node.next = l1
        else: node.next = l2
        return ret.next
