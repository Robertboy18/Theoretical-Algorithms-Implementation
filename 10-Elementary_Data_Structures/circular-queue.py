class CircularQueue:
	def init(self, max_size):
		self.items = [None] * max_size
		self.front = 0
		self.rear = 0
		self.max_size = max_size

	def enqueue(self, item):
		if (self.rear + 1) % self.max_size == self.front:
			print("Queue is full")
			return
		self.items[self.rear] = item
		self.rear = (self.rear + 1) % self.max_size

	def dequeue(self):
		if self.front == self.rear:
			print("Queue is empty")
			return
		item = self.items[self.front]
		self.items[self.front] = None
		self.front = (self.front + 1) % self.max_size
		return item

	def peek(self):
		return self.items[self.front]

	def is_empty(self):
		return self.front == self.rear

	def size(self):
		return (self.rear - self.front + self.max_size) % self.max_size