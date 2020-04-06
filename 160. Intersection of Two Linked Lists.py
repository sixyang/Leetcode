# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:return None       # 唉，每次都要在这一行栽一次……
        # la = set()
        # nodeA = headA
        # while nodeA:
        #     la.add(nodeA)
        #     nodeA = nodeA.next
        # nodeB = headB
        # head = None
        # count = 0
        # while nodeB:
        #     if nodeB in la:
        #         if count < 1:
        #             head = nodeB
        #         count += 1
        #     else:
        #         count = 0
        #         head = None
        #     nodeB = nodeB.next
        # return head

        # 这不是我写的，俺看不懂~
        pA, pB = headA, headB
        while pA != pB:
            pA = headB if pA == None else pA.next
            pB = headA if pB == None else pB.next
        return pA
