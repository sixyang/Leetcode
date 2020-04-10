# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 链表的题目就是麻烦，要非常小心，注意头和尾
        if not head:return None
        length = 1
        l = head
        while l.next:
            l = l.next
            length += 1
        k = length - k%length               # 这里因为会超过长度，所以需要加个 %
        if k == length:return head
        ret = node = head
        while k > 1:
            node = node.next
            k -= 1
        ret = position = node.next
        node.next = None
        while position.next:position = position.next
        position.next = head
        return ret
