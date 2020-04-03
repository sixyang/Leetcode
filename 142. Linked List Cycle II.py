# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 经典的哈希集合判重~
        # if not head:return None             # 又被这个特殊例子坑了一次。
        # s = set()
        # node = head
        # while node.next and node.next not in s:
        #     s.add(node)
        #     node = node.next
        # if node.next:return node.next
        # elif not node.next:return None

        #这个方法还是挺棒的！
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                # 相遇，slow指向head
                slow = head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
