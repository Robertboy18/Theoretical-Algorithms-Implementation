class Node:
	def init(self, value):
		self.value = value
		self.next = None

class LinkedList:
	def init(self):
		self.head = None

	def add_node(self, value):
		new_node = Node(value)
		if self.head is None:
			self.head = new_node
			return
		
		current_node = self.head
		while current_node.next is not None:
			current_node = current_node.next
		current_node.next = new_node

	def delete_node(self, value):
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
		current_node = self.head
		while current_node is not None:
			print(current_node.value)
			current_node = current_node.next