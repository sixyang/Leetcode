# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 这就是一道综合题，哈哈 😄
        # 这里用到了快慢指针获得中点
        if not head: return None
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow.next
        slow.next = None
        
        # 这里是反转链表
        prev = None
        while middle:
            middle.next, prev, middle = prev, middle, middle.next
        
        # 这里是合并两个链表
        middle = prev
        node = head
        while node and middle:
            next = node.next
            node.next = middle
            mnext = middle.next
            middle.next = next
            node = next
            middle = mnext
        # 将三个点合在一道题目里面，还是蛮有意思的~
