class Queue:
	def init(self):
		self.items = []

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		return self.items.pop(0)

	def peek(self):
		return self.items[0]

	def is_empty(self):
		return len(self.items) == 0

	def size(self):
		return len(self.items)

# Initiate
q = Queue()
q.enqueue(4)
q.enqueue('dog')
print(q.peek())