class MinStack:

    def __init__(self):
        self.stack = []
        self.min_index = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.stack[self.min_index]:
            self.min_index = len(self.stack)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_index]
