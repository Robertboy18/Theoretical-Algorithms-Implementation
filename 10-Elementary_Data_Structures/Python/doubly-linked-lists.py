import unittest

# Author: Robert Joseph


class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        """
        This class represents a node in a doubly linked list.
        Each node contains data, a reference to the next node, and a reference to the previous node.
        """
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:
    def __init__(self):
        """
        This class represents a doubly linked list.
        It contains a reference to the head (the first node) and the tail (the last node) of the list.
        """
        self.head = None
        self.tail = None

    def append(self, data):
        """
        Appends a new node with the given data to the end of the linked list.
        Time complexity: O(1)
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

    def prepend(self, data):
        """
        Prepends a new node with the given data to the beginning of the linked list.
        Time complexity: O(1)
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev_node = new_node
            new_node.next_node = self.head
            self.head = new_node

    def delete(self, data):
        """
        Deletes the first occurrence of a node with the given data from the linked list.
        Time complexity: O(n)
        """
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev_node is not None:
                    current_node.prev_node.next_node = current_node.next_node
                if current_node.next_node is not None:
                    current_node.next_node.prev_node = current_node.prev_node
                if current_node == self.head:
                    self.head = current_node.next_node
                if current_node == self.tail:
                    self.tail = current_node.prev_node
            current_node = current_node.next_node

    def search(self, data):
        """
        Searches for the first occurrence of a node with the given data in the linked list.
        Returns the node if found, None otherwise.
        Time complexity: O(n)
        """
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next_node
        return None

    def print_list(self):
        """
        Prints the elements of the linked list.
        Time complexity: O(n)
        """
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node


class TestLinkedList(unittest.TestCase):
    def test_linked_list(self):
        # Initialize the linked list
        linked_list = LinkedList()

        # Append nodes
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)

        # Test the print_list method
        self.assertEqual(linked_list.print_list(), None)  # No return value, so None is expected

        # Test the search method
        self.assertEqual(linked_list.search(2), linked_list.head.next_node)  # The second node should contain 2

        # Test the delete method
        linked_list.delete(2)
        self.assertEqual(linked_list.search(2), None)  # The node with data 2 should no longer exist


if __name__ == '__main__':
    unittest.main()
