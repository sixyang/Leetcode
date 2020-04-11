# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 为啥我的代码这么慢，没理由啊！
        if not head:return None             # 每次在这儿都要挂一次，woc！
        odd = head
        evenhead = even = odd.next if odd.next else None
        while odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenhead
        return head
