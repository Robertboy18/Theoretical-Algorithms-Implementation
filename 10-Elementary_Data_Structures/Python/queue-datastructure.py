import unittest

# Author: Robert Joseph

class Queue:
    def __init__(self):
        """
        This class represents a basic queue data structure.
        """
        self.items = []

    def enqueue(self, item):
        """
        Adds an item to the end of the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Removes and returns the first item from the queue.
        """
        return self.items.pop(0)

    def peek(self):
        """
        Returns the first item in the queue without removing it.
        """
        return self.items[0]

    def is_empty(self):
        """
        Checks if the queue is empty.
        Returns:
            - True if the queue is empty
            - False otherwise
        """
        return len(self.items) == 0

    def size(self):
        """
        Returns the number of items in the queue.
        """
        return len(self.items)


class TestQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        q = Queue()
        q.enqueue(4)
        q.enqueue('dog')
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.dequeue(), 'dog')

    def test_peek(self):
        q = Queue()
        q.enqueue(4)
        q.enqueue('dog')
        self.assertEqual(q.peek(), 4)

    def test_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(4)
        self.assertFalse(q.is_empty())

if __name__ == '__main__':
    unittest.main()
