import unittest

# Author: Robert Joseph

# Queue implementation
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Add the item to the end of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the first item from the queue
        return self.items.pop(0)

    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0

    def size(self):
        # Return the size of the queue
        return len(self.items)


# Stack implementation using two queues
class Stack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        # Add the item to queue1
        self.queue1.enqueue(item)

    def pop(self):
        # Move all items from queue1 to queue2, except the last one
        while self.queue1.size() > 1:
            self.queue2.enqueue(self.queue1.dequeue())

        # Return the last item in queue1 (which is the top of the stack)
        return self.queue1.dequeue()

    def peek(self):
        # Move all items from queue1 to queue2, except the last one
        while self.queue1.size() > 1:
            self.queue2.enqueue(self.queue1.dequeue())

        # Return the last item in queue1 (which is the top of the stack)
        item = self.queue1.dequeue()

        # Add the item back to queue1
        self.queue1.enqueue(item)

        return item

    def is_empty(self):
        return self.queue1.is_empty()

    def size(self):
        return self.queue1.size()


class TestStack(unittest.TestCase):
    def test_stack_operations(self):
        s = Stack()

        # Test with integers
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.peek(), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.size(), 1)
        self.assertFalse(s.is_empty())

        # Test with strings
        s.push('apple')
        s.push('banana')
        self.assertEqual(s.peek(), 'banana')
        self.assertEqual(s.pop(), 'banana')
        self.assertEqual(s.size(), 1)
        self.assertFalse(s.is_empty())

        # Test with mixed types
        s.push(4.5)
        s.push(True)
        self.assertEqual(s.peek(), True)
        self.assertEqual(s.pop(), True)
        self.assertEqual(s.size(), 2)
        self.assertFalse(s.is_empty())


if __name__ == '__main__':
    unittest.main()
