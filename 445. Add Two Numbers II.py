# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''思想：先遍历两个链表，用两个栈存储链表的节点(因为题目要求不能逆序，不能直接用 第2题的方法直接做)。然后遍历两个栈，pop()栈元素，进行相加后添加到新链表ret的next处。这样不断地循环，直到两个栈均空。要注意像 [9,9] [1] 的测试案例，遍历结束后flag仍然为1，也就是说要进位。最后将装有结果的栈pop，用ret.next = s.pop()即可得结果。
        代码写得比较麻烦，但是思路还是比较清楚的，另外还可以通过不创建新链表，只是对长链表进行修改来减少空间复杂度~'''
        n1, n2 = l1, l2
        s1, s2 = [], []
        r = ret = ListNode(None)
        flag = False
        while n1 or n2:
            if n1:
                s1.append(n1.val)
                n1 = n1.next
            if n2:
                s2.append(n2.val)
                n2 = n2.next
        s = []
        while s1 or s2:
            n1 = s1.pop() if s1 else 0
            n2 = s2.pop() if s2 else 0
            res = n1 + n2
            s.append(ListNode((res+flag)%10))
            flag = 1 if res+flag >= 10 else 0
        if flag:s.append(ListNode(1))
        while s:
            ret.next = s.pop()
            ret = ret.next
        return r.next            
