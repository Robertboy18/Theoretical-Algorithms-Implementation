import unittest

# Author: Robert Joseph

class CircularQueue:
    def __init__(self, max_size):
        """
        This function initializes a circular queue with a maximum size.
        """
        self.items = [None] * max_size
        self.front = 0
        self.rear = 0
        self.max_size = max_size

    def enqueue(self, item):
        """
        This function adds an item to the circular queue.
        """
        if (self.rear + 1) % self.max_size == self.front:
            print("Queue is full")
            return
        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.max_size

    def dequeue(self):
        """
        This function removes an item from the circular queue and returns it.
        """
        if self.front == self.rear:
            print("Queue is empty")
            return
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.max_size
        return item

    def peek(self):
        """
        This function returns the item at the front of the circular queue.
        """
        return self.items[self.front]

    def is_empty(self):
        """
        This function checks if the circular queue is empty.
        """
        return self.front == self.rear

    def size(self):
        """
        This function returns the current size of the circular queue.
        """
        return (self.rear - self.front + self.max_size) % self.max_size


class TestCircularQueue(unittest.TestCase):
    def test_circular_queue(self):
        # Test empty queue
        cq = CircularQueue(5)
        self.assertTrue(cq.is_empty())
        self.assertEqual(cq.size(), 0)

        # Test enqueue
        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)
        self.assertFalse(cq.is_empty())
        self.assertEqual(cq.size(), 3)

        # Test dequeue
        item = cq.dequeue()
        self.assertEqual(item, 1)
        self.assertEqual(cq.size(), 2)

        # Test peek
        peek_item = cq.peek()
        self.assertEqual(peek_item, 2)

        # Test full queue
        cq.enqueue(4)
        cq.enqueue(5)
        cq.enqueue(6)  # This should print "Queue is full"
        self.assertEqual(cq.size(), 4)


if __name__ == '__main__':
    unittest.main()
