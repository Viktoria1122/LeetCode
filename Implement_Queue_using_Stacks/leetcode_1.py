class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        self.stack1.push(x)

    def pop(self) -> int:
        if self.stack2.is_empty():
            self.transfer()
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2.is_empty():
            self.transfer()
        return self.stack2.peek()

    def empty(self) -> bool:
        return self.stack1.is_empty() and self.stack2.is_empty()

    def transfer(self):
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()