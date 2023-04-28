class Node:
	def init(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

class BinaryTree:
	def init(self, root=None):
		self.root = root

	def insert(self, value):
		new_node = Node(value)
		if self.root is None:
			self.root = new_node
			return
		current_node = self.root
		while True:
			if value <= current_node.value:
				if current_node.left is None:
					current_node.left = new_node
					return
				current_node = current_node.left
			else:
				if current_node.right is None:
					current_node.right = new_node
					return
				current_node = current_node.right

	def search(self, value):
		current_node = self.root
		while current_node is not None:
			if value == current_node.value:
				return True
			elif value < current_node.value:
				current_node = current_node.left
			else:
				current_node = current_node.right
		return False