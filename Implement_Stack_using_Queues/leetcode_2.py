class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        # Add the new element to the empty queue (either queue1 or queue2)
        if self.queue1.is_empty():
            self.queue1.enqueue(x)
            while not self.queue2.is_empty():
                self.queue1.enqueue(self.queue2.dequeue())
        else:
            self.queue2.enqueue(x)
            while not self.queue1.is_empty():
                self.queue2.enqueue(self.queue1.dequeue())

    def pop(self) -> int:
        if not self.queue1.is_empty():
            return self.queue1.dequeue()
        elif not self.queue2.is_empty():
            return self.queue2.dequeue()

    def top(self) -> int:
        if not self.queue1.is_empty():
            return self.queue1.peek()
        elif not self.queue2.is_empty():
            return self.queue2.peek()

    def empty(self) -> bool:
        return self.queue1.is_empty() and self.queue2.is_empty()
