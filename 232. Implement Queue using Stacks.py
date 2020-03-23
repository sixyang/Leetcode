class MyQueue:
    #队列实现栈感觉要复杂一些，但是栈实现队列还是挺简单的~但是我这边感觉复杂度比较高……
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.rstack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.rstack:
            self.rstack.extend(self.stack[::-1])
            self.stack.clear()              #就这里改成self.stack = []，然后时间就大大增加了？
        ret = self.rstack.pop()
        return ret

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.rstack:return self.rstack[-1]
        else:return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack and not self.rstack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
