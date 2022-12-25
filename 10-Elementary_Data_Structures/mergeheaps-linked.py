class Node:
	def init(self, value, next_node=None):
		self.value = value
		self.next_node = next_node

class LinkedList:
	def init(self):
		self.head = None

	def insert(self, value):
		new_node = Node(value)
		new_node.next_node = self.head
		self.head = new_node

	def merge(self, other_list):
		current_node = self.head
		other_node = other_list.head
		
		# Create a new linked list to hold the merged values
		merged_list = LinkedList()
		
		while current_node is not None and other_node is not None:
			if current_node.value < other_node.value:
				merged_list.insert(current_node.value)
				current_node = current_node.next_node
			else:
				merged_list.insert(other_node.value)
				other_node = other_node.next_node
		
		# Add any remaining nodes from either list
		while current_node is not None:
			merged_list.insert(current_node.value)
			current_node = current_node.next_node
		
		while other_node is not None:
			merged_list.insert(other_node.value)
			other_node = other_node.next_node
		
		return merged_list