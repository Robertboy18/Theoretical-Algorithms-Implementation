# Implement a linked list using a queue

class Node:
	def init(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def init(self):
		self.head = None

	def add_node(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		current = self.head
		while current.next is not None:
			current = current.next
		current.next = new_node

	def to_queue(self):
		queue = Queue()
		current = self.head
		while current is not None:
			queue.enqueue(current.data)
			current = current.next
		return queue