class MinStack:

    def __init__(self):
        self.stack = []
        self.min_index = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_index is None:
            self.min_index = 0
        elif val < self.stack[self.min_index]:
            self.min_index = len(self.stack) - 1

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_index]
