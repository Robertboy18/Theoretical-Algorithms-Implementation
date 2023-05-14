import math
import unittest

# Author : Robert Joseph

class min_max_heap:
    def __init__(self, arr):
        self.heap = arr

    def check(self):
        """
        This method checks if the heap is empty.
        """
        return len(self.heap) < 1

    def get_max(self):
        """
        This method returns the maximum element of the heap.
        """
        if not self.check():
            return self.heap[0]
        else:
            print("Empty Heap")

    def parent(self, i):
        """
        This method returns the parent of a node at index i.
        """
        if 0 <= math.floor((i-1)/2) < len(self.heap):
            return math.floor((i-1)/2)
        else:
            pass

    def right_child(self, i):
        """
        This method returns the index of the right child of a node at index i.
        """
        if 2*i+2 < len(self.heap):
            return 2*i+2
        else:
            return -1

    def left_child(self, i):
        """
        This method returns the index of the left child of a node at index i.
        """
        if 2*i+1 < len(self.heap):
            return 2*i+1
        else:
            return -1

    def check_index(self, i):
        """
        This method checks if an index is within the bounds of the heap.
        """
        if i < len(self.heap):
            return True
        else:
            False

    def heapify_max(self, i):
        """
        This function restores the max-heap property for the subtree rooted at index i.
        """
        current_max = i
        left = 2*i+1
        right = 2*i+2

        # Check if left child is greater than current node
        if current_max < len(self.heap) and self.check_index(left) and self.heap[i] < self.heap[left]:
            current_max = left

        # Check if right child is greater than current max
        if current_max < len(self.heap) and self.check_index(right) and self.heap[current_max] < self.heap[right]:
            current_max = right

        # Swap current node with child if current node is not the max
        if current_max != i:
            self.heap[i], self.heap[current_max] = self.heap[current_max], self.heap[i]
            self.heapify_max(current_max)

    def max_heap(self):
        """
        This function converts the heap to a max-heap.
        """
        for i in range(math.ceil(len(self.heap)/2)-1, -1, -1):
            self.heapify_max(i)

    def heapify_min(self, i):
        """
        This function restores the min-heap property for the subtree rooted at index i.
        """
        current_min = i
        left = 2*i+1
        right = 2*i+2

        # Check if left child is less than current node
        if current_min < len(self.heap) and self.check_index(left) and self.heap[i] > self.heap[left]:
            current_min = left

        # Check if right child is less than current min
        if current_min < len(self.heap) and self.check_index(right) and self.heap[current_min] > self.heap[right]:
            current_min = right

        # Swap current node with child if current node is not the min
        if current_min != i:
            self.heap[i], self.heap[current_min] = self.heap[current_min], self.heap[i]
            self.heapify_min(current_min)

    def min_heap(self):
        """
        This function converts the heap to a min-heap.
        """
        for i in range(math.ceil(len(self.heap)/2), -1, -1):
            self.heapify_min(i)

    def insert(self, val):
        """
        This function inserts a value into the heap.
        """
        self.heap.append(val)

    def pop(self):
        """
        This function removes the root of the heap.
        """
        if not self.check():
            self.heap.pop(0)
            self.max_heap()
        else:
            print("Empty Heap")

    def min_heap_convert(self):
        """
        This function converts the heap to a min-heap.
        """
        self.min_heap()

    def heapsort(self, reversed=False):
        """
        This function performs heapsort on the heap and returns a sorted array.
        """
        sorted_array = []
        for __ in range(len(self.heap)):
            sorted_array.append(self.heap.pop(0))
            self.max_heap()
        if not reversed:
            return sorted_array
        else:
            return sorted_array[::-1]

    def print_heap(self):
        """
        This function prints the heap.
        """
        print("Heap is : ", self.heap)

    def replace(self, x, val):
        """
        This function replaces a value
        """
        for i in range(len(self.heap)):
            if self.heap[i] == x:
                self.heap[i] = val

			
class TestMinMaxHeap(unittest.TestCase):
    def test_min_max_heap(self):
        # Test with a small list
        t = [2, 1, 3]
        z = min_max_heap(t)
        print("Sorted", z.heapsort())
        self.assertEqual(z.heapsort(), [1, 2, 3])

        # Test with a large list
        t = [16, 14, 4, 3, 2, 1]
        z = min_max_heap(t)
        self.assertEqual(z, [1, 2, 4, 16, 3, 14])

        # Test with a list of duplicates
        t = [1, 2, 3, 3, 2, 1]
        z = min_max_heap(t)
        self.assertEqual(z, [1, 2, 1, 3, 2, 3])


if __name__ == '__main__':
    unittest.main()
