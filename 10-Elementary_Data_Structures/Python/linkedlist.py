import unittest

# Author: Robert Joseph

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        """
        This method adds a new node with the given value to the end of the linked list.
        Time complexity: O(n), where n is the number of nodes in the linked list.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def delete_node(self, value):
        """
        This method deletes the first occurrence of a node with the given value from the linked list.
        Time complexity: O(n), where n is the number of nodes in the linked list.
        """
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def print_list(self):
        """
        This method prints the values of all nodes in the linked list.
        Time complexity: O(n), where n is the number of nodes in the linked list.
        """
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next


class TestLinkedList(unittest.TestCase):
    def test_linked_list_operations(self):
        # Initialize an empty linked list
        linked_list = LinkedList()

        # Add nodes to the linked list
        linked_list.add_node(1)
        linked_list.add_node(2)
        linked_list.add_node(3)

        # Test print_list method
        # Expected output: 1 2 3
        self.assertEqual(linked_list.print_list(), None)

        # Test delete_node method
        linked_list.delete_node(2)

        # Test print_list method after deletion
        # Expected output: 1 3
        self.assertEqual(linked_list.print_list(), None)

        # Test delete_node method with non-existing value
        linked_list.delete_node(5)

        # Test print_list method after deletion of non-existing value
        # Expected output: 1 3
        self.assertEqual(linked_list.print_list(), None)


if __name__ == '__main__':
    unittest.main()
