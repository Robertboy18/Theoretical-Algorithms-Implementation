import heapq
import unittest

# Author: Robert Joseph

def find_ith_largest(A, i):
    """
    This function finds the i-th largest element in the list A using a max heap.
    """
    # Build a max heap from A
    heap = [-x for x in A]
    heapq.heapify(heap)

    # Extract the i-1 largest elements from the heap
    for j in range(i-1):
        heapq.heappop(heap)

    # The i-th largest element is now at the root of the heap
    return -heapq.heappop(heap)


class TestFindIthLargest(unittest.TestCase):
    def test_find_ith_largest(self):
        # Test with list A = [3, 2, 1, 5, 4, 6, 7, 8, 9, 10], i = 3
        A = [3, 2, 1, 5, 4, 6, 7, 8, 9, 10]
        i = 3
        self.assertEqual(find_ith_largest(A, i), 8)

        # Test with list A = [9, 3, 2, 7, 6, 1, 4, 5, 10, 8], i = 5
        A = [9, 3, 2, 7, 6, 1, 4, 5, 10, 8]
        i = 5
        self.assertEqual(find_ith_largest(A, i), 6)

        # Test with list A = [1, 2, 3, 4, 5], i = 1
        A = [1, 2, 3, 4, 5]
        i = 1
        self.assertEqual(find_ith_largest(A, i), 5)


if __name__ == '__main__':
    unittest.main()
