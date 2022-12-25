# Description: Stack implementation using a linked list

class Node:
	def init(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def init(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def pop(self):
		if self.head is None:
			return None
		popped = self.head.data
		self.head = self.head.next
		return popped

	def peek(self):
		if self.head is None:
			return None
		return self.head.data

	def is_empty(self):
		return self.head is None

	def size(self):
		count = 0
		current = self.head
		while current is not None:
			count += 1
			current = current.next
		return count