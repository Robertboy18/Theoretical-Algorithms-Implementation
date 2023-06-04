import unittest

# Author: Robert Joseph

class Node:
    def __init__(self, value, next_node=None):
        """
        This class represents a node in a linked list.
        """
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        """
        This class represents a linked list.
        """
        self.head = None

    def insert(self, value):
        """
        Inserts a new node with the given value at the beginning of the linked list.
        Time Complexity: O(1)
        """
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def merge(self, other_list):
        """
        Merges the current linked list with another linked list in sorted order.
        Returns a new merged linked list.
        Time Complexity: O(n + m), where n and m are the lengths of the current and other linked lists, respectively.
        """
        current_node = self.head
        other_node = other_list.head

        # Create a new linked list to hold the merged values
        merged_list = LinkedList()

        while current_node is not None and other_node is not None:
            if current_node.value < other_node.value:
                merged_list.insert(current_node.value)
                current_node = current_node.next_node
            else:
                merged_list.insert(other_node.value)
                other_node = other_node.next_node

        # Add any remaining nodes from either list
        while current_node is not None:
            merged_list.insert(current_node.value)
            current_node = current_node.next_node

        while other_node is not None:
            merged_list.insert(other_node.value)
            other_node = other_node.next_node

        return merged_list


class TestLinkedList(unittest.TestCase):
    def test_merge(self):
        # Test with two linked lists: [1, 3, 5] and [2, 4, 6]
        linked_list1 = LinkedList()
        linked_list1.insert(5)
        linked_list1.insert(3)
        linked_list1.insert(1)

        linked_list2 = LinkedList()
        linked_list2.insert(6)
        linked_list2.insert(4)
        linked_list2.insert(2)

        merged_list = linked_list1.merge(linked_list2)
        self.assertEqual(merged_list.head.value, 1)
        self.assertEqual(merged_list.head.next_node.value, 2)
        self.assertEqual(merged_list.head.next_node.next_node.value, 3)
        self.assertEqual(merged_list.head.next_node.next_node.next_node.value, 4)
        self.assertEqual(merged_list.head.next_node.next_node.next_node.next_node.value, 5)
        self.assertEqual(merged_list.head.next_node.next_node.next_node.next_node.next_node.value, 6)

        # Test with two empty linked lists
        linked_list3 = LinkedList()
        linked_list4 = LinkedList()

        merged_list = linked_list3.merge(linked_list4)
        self.assertIsNone(merged_list.head)

        # Test with one empty linked list and one non-empty linked list
        linked_list5 = LinkedList()
        linked_list6 = LinkedList()
        linked_list6.insert(2)
        linked_list6.insert(1)

        merged_list = linked_list5.merge(linked_list6)
        self.assertEqual(merged_list.head.value, 1)
        self.assertEqual(merged_list.head.next_node.value, 2)


if __name__ == '__main__':
    unittest.main()
