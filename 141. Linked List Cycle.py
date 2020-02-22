# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''我这边是每次迭代就用HashSet记下当前节点，但是如果可以改变链表结构的话，可以直接通过赋值改变节点，统一节点的值，然后再遍历的时候，如果节点为统一的值则说明存在环。否则就没有。（但是改变链表结构。emmm）'''
        # s = set()
        # while head:
        #     if head in s:return True
        #     s.add(head)
        #     head = head.next
        # return False
        
        '''这串代码的细节实在是太多了，正如链表一般，链表要考虑next，还有开头的特殊情况。'''
        if not head or not head.next:return False           #去除杂数据
        slow, fast = head, head.next                        #这边要写head.next，不然会报错
        # while slow != fast:                               #这边条件是可以改的。
        while fast and fast.next:
            # if not fast or not fast.next:return False
            if fast == slow:return True
            slow = slow.next
            fast = fast.next.next
        return False
