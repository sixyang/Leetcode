# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def __init__(self):               
    '''这是以前刚开始做题的时候用列表来做的……现在已经没法通过了……'''
    #     self.li = []
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    # #     self.recursion(head)
    # #     pass
    #     self.recursion(head)
    #     self.li.pop(-n)
    #     return self.li
    # def recursion(self,lian):
    #     if lian.next:
    #         self.li.append(lian.val)
    #         self.recursion(lian.next)
    #     else:self.li.append(lian.val)

    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    ''' 哎，果然链表递归还是不熟练啊，md，写了这么多。别人只要5行就搞定…… 不过，之所以要这么多变量，是因为自己对作用域还不太熟悉，以为弄个global就行了，但是还是报错。emmmm'''
    #     def recursion(head, times, n, length, rhead):
    #         if not head:
    #             return times, length, rhead
    #         length += 1
    #         times, length, rhead = recursion(head.next, times, n, length, rhead)
    #         if n == length and times+1 == n:rhead = True
    #         times += 1
    #         if times == n+1:head.next = head.next.next
    #         return times, length, rhead
    #     t = recursion(head, 0, n, 0, False)
    #     if t[-1] == True:head = head.next
    #     return head
    
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    '''这是改编的别人的cpp代码，python这里直接用global好像不行，emmm，需要在递归里面传入cur。'''
    #     def recursion(head, n, cur):
    #         if not head:return None
    #         head.next = recursion(head.next, n, cur)
    #         cur += 1
    #         if n == cur:return head.next
    #         return head
    #     head = recursion(head, n, 0)
    #     return head

    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    '''这个思路真的是完美，快慢指针在这里运用的淋漓尽致~'''
    #     fast, slow = head, head
    #     while n > 0:
    #         fast = fast.next
    #         n -= 1
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next
    #     if fast:slow.next = slow.next.next
    #     else:head = head.next
    #     return head

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def removeNode(node, int):
            if not node.next:return 1
            m = removeNode(node.next, n)
            if m == n:
                if m == 1:node.next = None
                else:node.next = node.next.next
            return m + 1
        return head.next if removeNode(head, n) == n else head
