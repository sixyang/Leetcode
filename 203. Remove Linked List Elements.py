# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # if not head:return None                 #每次都要在这儿栽一回……
        # while head and head.val == val:head = head.next     # 链表的题目一定要考虑 头结点和None！
        # prev, node = ListNode(None), head
        # prev.next = head
        # while node:
        #     if node.val == val:
        #         prev.next = node.next
        #     else:prev = prev.next
        #     node = node.next
        # return head

        if not head:return head         # 这串代码是排名第一的人写的，真的是骚的不行~果然链表还是用递归好一些啊！QWQ但是不擅长递归，个人能用循环的就用循环QAQ
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
