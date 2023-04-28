class Node:
	def init(self, data=None, next_node=None, prev_node=None):
		self.data = data
		self.next_node = next_node
		self.prev_node = prev_node

class LinkedList:
	def init(self):
		self.head = None
		self.tail = None

	def append(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next_node = new_node
			new_node.prev_node = self.tail
			self.tail = new_node

	def prepend(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.head.prev_node = new_node
			new_node.next_node = self.head
			self.head = new_node

	def delete(self, data):
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
		current_node = self.head
		while current_node is not None:
			if current_node.data == data:
				return current_node
			current_node = current_node.next_node
		return None

	def print_list(self):
		current_node = self.head
		while current_node is not None:
			print(current_node.data)
			current_node = current_node.next_node