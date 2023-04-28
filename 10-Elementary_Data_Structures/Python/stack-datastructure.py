class Stack:
	def init(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def is_empty(self):
		return len(self.items) == 0

	def size(self):
		return len(self.items)

# Initiate
s = Stack()
s.push(4)
s.push('dog')
print(s.peek())