class Node():
    #一道题目花了超过5个小时，唉，不达目的誓不罢休。不过做完了还是挺爽的，有那种茅塞顿开的感觉，这就是学习的乐趣所在。哈哈哈
    def __init__(self, val, next):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(None, None)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.head
        if index < 0:return -1
        while index > 0 and node:
            index -= 1
            node = node.next
        if not node:return -1
        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head.val == None:
            self.head.val = val
        else:
            back = self.head
            prev = Node(val, back)
            self.head = prev

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head.val == None:
            self.head.val = val
        else:
            node = self.head
            while node.next:
                node = node.next
            else:node.next = Node(val, None)   

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index <= 0:self.addAtHead(val)
        else:
            node = self.head
            while index > 1 and node.next:
                node = node.next
                index -= 1
            if index <= 1:
                back = node.next
                node.next = Node(val, back)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > 0:
            node = self.head
            while index > 1 and node.next:
                index -= 1
                node = node.next
            if node.next:node.next = node.next.next  
        elif index == 0:
            self.head = self.head.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
