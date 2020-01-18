# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast.next:
            if fast.next.next:
                fast = fast.next.next
            else:
                fast = fast.next
            slow = slow.next
        return slow
