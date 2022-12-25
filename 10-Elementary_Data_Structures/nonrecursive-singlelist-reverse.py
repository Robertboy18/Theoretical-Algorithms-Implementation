# constant time complexity reversing a single linked list

from linkedlist import LinkedList, Node

def reverse_linked_list(head):
	# Initialize variables for the new head and the current node
	new_head = None
	curr = head

	Copy code
	# Iterate through the linked list, reversing the "next" pointers as we go
	while curr:
		temp = curr.next
		curr.next = new_head
		new_head = curr
		curr = temp

	# Return the new head of the reversed list
	return new_head

# Test
ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
ll.add_node(5)
head = reverse_linked_list(ll.head)
ll.print_list()