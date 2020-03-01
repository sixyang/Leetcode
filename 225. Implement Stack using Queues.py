class MyStack:
    #打卡！3月1号~一开始没看题目，直接用的队列，pop，append……很快就实现了，但是看了一眼题目，woc？就只能用队列默认的四个方法？？？emmmm，只能重新写了。
    #两个队列实现栈，两个栈实现队列
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.queue = deque()
        self.rqueue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.queue) == 1:return self.queue.popleft()
        elif len(self.queue) < 1:
            self.queue, self.rqueue = self.rqueue, self.queue
        for _ in range(len(self.queue)-1):
            val = self.queue.popleft()
            self.rqueue.append(val)
        ret = self.queue.popleft()
        return ret

    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.queue) == 1:
            ret = self.queue.popleft()
            self.queue.append(ret)
            return ret
        if len(self.queue) < 1:
            self.queue, self.rqueue = self.rqueue, self.queue
        for _ in range(len(self.queue)-1):
            val = self.queue.popleft()
            self.rqueue.append(val)
        ret = self.queue.popleft()
        self.rqueue.append(ret)
        self.queue, self.rqueue = self.rqueue, self.queue
        return ret            


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return False if len(self.queue) or len(self.rqueue) else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
