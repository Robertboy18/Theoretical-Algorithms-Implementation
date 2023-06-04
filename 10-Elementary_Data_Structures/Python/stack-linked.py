import unittest

# Author: Robert Joseph

# Node class represents a node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class represents a stack implemented using a linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # Pushes an element onto the stack
    def push(self, data):
        """
        Pushes an element onto the stack.
        Time complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Pops an element from the stack
    def pop(self):
        """
        Pops an element from the stack.
        Time complexity: O(1)
        """
        if self.head is None:
            return None
        popped = self.head.data
        self.head = self.head.next
        return popped

    # Peeks at the top element of the stack
    def peek(self):
        """
        Returns the top element of the stack without removing it.
        Time complexity: O(1)
        """
        if self.head is None:
            return None
        return self.head.data

    # Checks if the stack is empty
    def is_empty(self):
        """
        Checks if the stack is empty.
        Time complexity: O(1)
        """
        return self.head is None

    # Returns the size of the stack
    def size(self):
        """
        Returns the number of elements in the stack.
        Time complexity: O(n), where n is the number of elements in the stack.
        """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count


class TestLinkedList(unittest.TestCase):
    def test_push_and_pop(self):
        stack = LinkedList()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)

    def test_peek(self):
        stack = LinkedList()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)

    def test_is_empty(self):
        stack = LinkedList()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

        
if __name__ == '__main__':
    unittest.main()
