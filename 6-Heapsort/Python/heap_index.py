import unittest
import math

# Author: Robert Joseph

def heap_index(t, i):
    """
    This function prints the indices of the head node, left child, and right child
    of a binary heap represented as a list t, given the index i of a node in the heap.
    """
    try:
        # index of the head node of the current node
        head_index = math.floor(i/2-1)
        print("Head Node at : ", t[head_index])
        
        # index of the left child of the current node
        left_index = 2*i + 1
        print("Left Child at : ", t[left_index])
        
        # index of the right child of the current node
        right_index = 2*i + 2
        print("Right Child at : ", t[right_index])
    
    except:
        print("No node present")

class TestHeapIndex(unittest.TestCase):
    def test_heap_index(self):
        # Test with a binary heap represented as a list
        t = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

        # Test with a node in the middle of the heap
        self.assertEqual(heap_index(t, 4), None)

        # Test with the last node in the heap
        self.assertEqual(heap_index(t, 9), None)

        # Test with a node that doesn't exist in the heap
        self.assertEqual(heap_index(t, 10), None)

if __name__ == '__main__':
    unittest.main()
