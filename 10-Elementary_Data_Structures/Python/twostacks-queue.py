import unittest

# Author: Robert Joseph


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        # Move all items from stack1 to stack2
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        # Pop the first item (which is the last item added to stack1) from stack2
        item = self.stack2.pop()
        # Move all items back to stack1
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())
        return item

    def peek(self):
        # Move all items from stack1 to stack2
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        # Peek at the first item (which is the last item added to stack1) in stack2
        item = self.stack2.peek()
        # Move all items back to stack1
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())
        return item

    def is_empty(self):
        return self.stack1.is_empty()

    def size(self):
        return self.stack1.size()


class TestQueue(unittest.TestCase):
    def test_queue(self):
        # Create a queue
        q = Queue()

        # Enqueue items
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        # Test dequeue
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)

        # Test peek
        self.assertEqual(q.peek(), 3)

        # Test size
        self.assertEqual(q.size(), 1)


if __name__ == '__main__':
    unittest.main()
