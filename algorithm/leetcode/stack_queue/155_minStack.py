class MinStack:

    def __init__(self):
        self.inner_list = []

    def push(self, val: int) -> None:
        self.inner_list.append(val)

    def pop(self) -> None:
        return self.inner_list.pop(-1)

    def top(self) -> int:
        return self.inner_list[-1]

    def getMin(self) -> int:
        return min(self.inner_list)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
