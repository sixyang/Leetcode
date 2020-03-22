class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.smallest = float('inf')
        

    def push(self, x: int) -> None:
        self.nums.append(x)
        if self.smallest > x:
            self.smallest = x

    def pop(self) -> None:
        if len(self.nums) > 0:
            top_num = self.nums.pop()
            if len(self.nums) > 0 and top_num == self.smallest:
                self.smallest = min(self.nums)
            elif len(self.nums) == 0:
                self.smallest = float('inf')
        else:
            return None

    def top(self) -> int:
        if len(self.nums) > 0:
            return self.nums[-1]
        else:
            return None

    def getMin(self) -> int:
        return self.smallest


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
