import unittest
from queue import Queue

# Author: Robert Joseph

class Node:
    def __init__(self, data):
        """
        This class represents a node in a linked list.
        Each node contains data and a reference to the next node.
        """
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """
        This class represents a linked list.
        It maintains a reference to the head node of the list.
        """
        self.head = None

    def add_node(self, data):
        """
        This method adds a new node with the given data at the end of the linked list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def to_queue(self):
        """
        This method converts the linked list to a queue.
        It iterates through the linked list and enqueues each node's data into the queue.
        """
        queue = Queue()
        current = self.head
        while current is not None:
            queue.put(current.data)
            current = current.next
        return queue


class TestLinkedList(unittest.TestCase):
    def test_to_queue(self):
        # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
        linked_list = LinkedList()
        linked_list.add_node(1)
        linked_list.add_node(2)
        linked_list.add_node(3)
        linked_list.add_node(4)
        linked_list.add_node(5)

        # Convert the linked list to a queue
        queue = linked_list.to_queue()

        # Test the elements in the queue
        self.assertEqual(queue.get(), 1)
        self.assertEqual(queue.get(), 2)
        self.assertEqual(queue.get(), 3)

        # Ensure the queue is empty after retrieving all elements
        self.assertTrue(queue.empty())


if __name__ == '__main__':
    unittest.main()
