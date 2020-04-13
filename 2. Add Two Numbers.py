# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 虽然写的比较烂，但是至少能出结果，哈哈。我记得这道题目我提交了18次。啧啧
        node1, node2 = l1, l2
        carry = False
        ret = head = ListNode(None)
        while node1 and node2:
            val = node1.val + node2.val
            if carry:val += 1
            if val >= 10:
                carry = True
                val = val % 10
            else:carry = False
            ret.next = ListNode(val)
            ret = ret.next
            node1 = node1.next
            node2 = node2.next
        node = node1 if node1 else node2
        while node:
            if carry:
                val = node.val+1
                if val < 10:
                    ret.next = ListNode(val)
                    carry = False
                else:
                    ret.next = ListNode(val%10)
                    ret.next.next = ListNode(1)
            else:
                ret.next = ListNode(node.val)
            ret = ret.next
            node = node.next
            
        if carry:ret.next = ListNode(1)
        return head.next
