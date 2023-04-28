# Show how to implement a stack using two queues.

class Stack:
	def init(self):
		self.queue1 = Queue()
		self.queue2 = Queue()

	def push(self, item):
		# Add the item to queue1
		self.queue1.enqueue(item)

	def pop(self):
		# Move all items from queue1 to queue2, except the last one
		while self.queue1.size() > 1:
			self.queue2.enqueue(self.queue1.dequeue())
		
		# Return the last item in queue1 (which is the top of the stack)
		return self.queue1.dequeue()

	def peek(self):
		# Move all items from queue1 to queue2, except the last one
		while self.queue1.size() > 1:
			self.queue2.enqueue(self.queue1.dequeue())
		
		# Return the last item in queue1 (which is the top of the stack)
		item = self.queue1.dequeue()
		
		# Add the item back to queue1
		self.queue1.enqueue(item)
		
		return item

	def is_empty(self):
		return self.queue1.is_empty()

	def size(self):
		return self.queue1.size()

# Initiate
s = Stack()
s.push(4)
s.push('dog')
print(s.peek())
