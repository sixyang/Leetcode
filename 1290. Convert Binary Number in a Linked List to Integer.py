# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # ret = ''
        # while head:
        #     ret += str(head.val)
        #     head = head.next
        # return int(ret, 2)
        ret = 0
        while head:
            ret <<= 1
            ret |= head.val
            head = head.next
        return  ret
