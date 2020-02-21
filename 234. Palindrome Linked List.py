# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #感觉现在leetcode的判题时间都增加了，之前都不到100ms的，最近很多题目都超过100ms。。。相同的代码。很奇怪……
        ret_list = []
        while head:
            ret_list.append(head.val)
            head = head.next
        # length = len(ret_list)
        # return ret_list[:length//2][::-1] == ret_list[length//2:] if length % 2 == 0 else ret_list[:length//2] == ret_list[length//2+1:][::-1]
        return ret_list == ret_list[::-1]
