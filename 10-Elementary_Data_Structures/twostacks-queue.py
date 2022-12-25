# Show how to implement a queue using two stacks

class Queue:
	def init(self):
		self.stack1 = Stack()
		self.stack2 = Stack()

	def enqueue(self, item):
		self.stack1.push(item)

	def dequeue(self):
		# Move all items from stack1 to stack2
		while not self.stack1.is_empty():
			self.stack2.push(self.stack1.pop())
		# Pop the first item (which is the last item added to stack1) from stack2
		item = self.stack2.pop()
		# Move all items back to stack1
		while not self.stack2.is_empty():
			self.stack1.push(self.stack2.pop())
		return item

	def peek(self):
		# Move all items from stack1 to stack2
		while not self.stack1.is_empty():
			self.stack2.push(self.stack1.pop())
		# Peek at the first item (which is the last item added to stack1) in stack2
		item = self.stack2.peek()
		# Move all items back to stack1
		while not self.stack2.is_empty():
			self.stack1.push(self.stack2.pop())
		return item

	def is_empty(self):
		return self.stack1.is_empty()

	def size(self):
		return self.stack1.size()

# Initiate
q = Queue()
q.enqueue(4)
q.enqueue('dog')
print(q.peek())