# Author : Robert Joseph
# Date : 13/02/2021
# Copyright - MIT License

import math

class min_max_heap:
	def __init__(self,arr):
		self.heap = arr
	
	def check(self):
		return len(self.heap) < 1

	def get_max(self):
		if not self.check():
			return self.heap[0]
		else:
			print("Empty Heap")

	def parent(self,i):
		if 0 <= math.floor((i-1)/2) < len(self.heap):
			return math.floor((i-1)/2)
		else:
			pass

	def right_child(self,i):
		if 2*i+2 < len(self.heap):
			return 2*i+2
		else:
			return -1

	def left_child(self,i):
		if 2*i+1 < len(self.heap):
			return 2*i+1
		else:
			return -1
	
	def check_index(self,i):
		if i < len(self.heap):
			return True
		else:
			False

	def heapify_max(self,i):
		current_max = i
		left = 2*i+1
		right = 2*i+2
		if current_max < len(self.heap) and self.check_index(left) and self.heap[i] < self.heap[left]:
			current_max = left
		if current_max < len(self.heap) and self.check_index(right) and self.heap[current_max] < self.heap[right]:
			current_max = right
		if current_max != i:
			self.heap[i],self.heap[current_max] = self.heap[current_max],self.heap[i]
			self.heapify_max(current_max)

	def max_heap(self):
		for i in range(math.ceil(len(self.heap)/2)-1,-1,-1):
			self.heapify_max(i)

	def heapify_min(self,i):
		current_min = i
		left = 2*i+1
		right = 2*i+2
		if current_min < len(self.heap) and self.check_index(left) and self.heap[i] > self.heap[left]:
			current_min = left
		if current_min < len(self.heap) and self.check_index(right) and self.heap[current_min] > self.heap[right]:
			current_min = right
		if current_min != i:
			self.heap[i],self.heap[current_min] = self.heap[current_min],self.heap[i]
			self.heapify_min(current_min)

	def min_heap(self):
		for i in range(math.ceil(len(self.heap)/2),-1,-1):
			self.heapify_min(i)

	def insert(self,val):
		self.heap.append(val)

	def pop(self):
		if not self.check():
			self.heap.pop(0)
			self.max_heap()
		else:
			print("Empty Heap")

	def min_heap_convert(self):
		self.min_heap()

	def heapsort(self,reversed = False):
		sorted_array = []
		for __ in range(len(self.heap)):
			sorted_array.append(self.heap.pop(0))
			self.max_heap()
		if not reversed:
			return sorted_array
		else:
			return sorted_array[::-1]

	def print_heap(self):
		print("Heap is : ", self.heap)

	def replace(self,x,val):
		for i in range(len(self.heap)):
			if self.heap[i] == x:
				self.heap[i] = val
			
t = [2]
z = min_max_heap(t)
z.insert(1)
z.insert(3)
z.insert(16)
z.insert(14)
z.insert(4)
z.max_heap()
z.print_heap()
print("Heapsort : ",z.heapsort(True))
