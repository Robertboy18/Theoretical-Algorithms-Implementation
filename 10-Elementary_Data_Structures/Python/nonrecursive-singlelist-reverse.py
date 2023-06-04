import unittest
from linkedlist import LinkedList, Node

# Author: Robert Joseph

def reverse_linked_list(head):
    """
    This function reverses a singly linked list in-place and returns the new head of the reversed list.
    It has a constant time complexity.
    """
    # Initialize variables for the new head and the current node
    new_head = None
    curr = head

    # Iterate through the linked list, reversing the "next" pointers as we go
    while curr:
        temp = curr.next
        curr.next = new_head
        new_head = curr
        curr = temp

    # Return the new head of the reversed list
    return new_head


class TestReverseLinkedList(unittest.TestCase):
    def test_reverse_linked_list(self):
        # Test with linked list: 1 -> 2 -> 3 -> 4 -> 5
        ll = LinkedList()
        ll.add_node(1)
        ll.add_node(2)
        ll.add_node(3)
        ll.add_node(4)
        ll.add_node(5)
        head = reverse_linked_list(ll.head)
        self.assertEqual(head.value, 5)  # New head should be 5
        self.assertEqual(head.next.value, 4)
        self.assertEqual(head.next.next.value, 3)
        self.assertEqual(head.next.next.next.value, 2)
        self.assertEqual(head.next.next.next.next.value, 1)

        # Test with linked list: 1 -> 2
        ll = LinkedList()
        ll.add_node(1)
        ll.add_node(2)
        head = reverse_linked_list(ll.head)
        self.assertEqual(head.value, 2)  # New head should be 2
        self.assertEqual(head.next.value, 1)

        # Test with an empty linked list
        ll = LinkedList()
        head = reverse_linked_list(ll.head)
        self.assertIsNone(head)  # Head should be None for an empty list


if __name__ == '__main__':
    unittest.main()
