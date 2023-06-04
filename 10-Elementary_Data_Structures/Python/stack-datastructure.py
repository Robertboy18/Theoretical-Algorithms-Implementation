import unittest

# Author: Robert Joseph

class Stack:
    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.items = []

    def push(self, item):
        """
        Adds an item to the top of the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the item from the top of the stack.
        """
        return self.items.pop()

    def peek(self):
        """
        Returns the item from the top of the stack without removing it.
        """
        return self.items[-1]

    def is_empty(self):
        """
        Checks if the stack is empty.
        """
        return len(self.items) == 0

    def size(self):
        """
        Returns the number of items in the stack.
        """
        return len(self.items)


class TestStack(unittest.TestCase):
    def test_stack_operations(self):
        # Create a stack
        s = Stack()

        # Test is_empty() on an empty stack
        self.assertTrue(s.is_empty())

        # Test push() and peek()
        s.push(4)
        self.assertEqual(s.peek(), 4)
        s.push('dog')
        self.assertEqual(s.peek(), 'dog')

        # Test size()
        self.assertEqual(s.size(), 2)

        # Test pop()
        self.assertEqual(s.pop(), 'dog')
        self.assertEqual(s.peek(), 4)
        self.assertEqual(s.size(), 1)
        self.assertFalse(s.is_empty())


if __name__ == '__main__':
    unittest.main()
