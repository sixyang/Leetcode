class MyCircularQueue:
    #我认认真真写的循环队列竟然不如别人的pop(0)？？？这也太离谱了吧。果然内置的东西还是快啊。
    # def __init__(self, k: int):
    #     """
    #     Initialize your data structure here. Set the size of the queue to be k.
    #     """
    #     self.queue = [-1 for i in range(k)]
    #     self.head, self.tail = 0, 0
    #     self.k = k

    # def enQueue(self, value: int) -> bool:
    #     """
    #     Insert an element into the circular queue. Return true if the operation is successful.
    #     """
    #     if not self.isFull():
    #         if self.tail == self.k:
    #             self.tail = 0
    #         self.queue[self.tail] = value
    #         self.tail += 1
    #         return True
    #     else:return False
            
    # def deQueue(self) -> bool:
    #     """
    #     Delete an element from the circular queue. Return true if the operation is successful.
    #     """
    #     if not self.isEmpty():
    #         if self.head == self.k:
    #             self.head = 0
    #         self.queue[self.head] = -1
    #         self.head += 1
    #         return True
    #     return False

    # def Front(self) -> int:
    #     """
    #     Get the front item from the queue.
    #     """
    #     if not self.isEmpty():
    #         return self.queue[self.head]        #这边需要是self.head!
    #     return -1

    # def Rear(self) -> int:
    #     """
    #     Get the last item from the queue.
    #     """
    #     if not self.isEmpty():
    #         return self.queue[self.tail-1]      #这边需要是self.tail-1!
    #     return -1
        
    # def isEmpty(self) -> bool:
    #     """
    #     Checks whether the circular queue is empty or not.
    #     """
    #     if len(set(self.queue)) == 1 and self.queue[0] == -1:return True
    #     else:return False

    # def isFull(self) -> bool:
    #     """
    #     Checks whether the circular queue is full or not.
    #     """
    #     if -1 not in set(self.queue):return True
    #     return False

    def __init__(self, k: int):
        self.que = []
        self.length = k
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if len(self.que) == self.length:
            return False
        self.que.append(value)
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if len(self.que) == 0:
            return False
        self.que.pop(0)
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if not self.que:
            return -1
        return self.que[0]    

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if not self.que:
            return -1
        return  self.que[-1]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if not self.que:
            return True
        return False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if len(self.que) == self.length:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
