import math
import unittest

# Author: Robert Joseph

def merge(A, p, q, r):
    """
    This function merges two subarrays of A: A[p..q] and A[q+1..r], 
    where p <= q < r. It assumes that the two subarrays are already sorted.
    """
    n1 = q - p + 1
    n2 = r - q

    # create two temporary arrays L and R
    L, R = [0] * (n1 + 1), [0] * (n2 + 1)
    
    # copy the elements from A into L and R
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]
    
    # set the last element of each array to infinity
    L[n1] = math.inf
    R[n2] = math.inf
    
    # merge the two subarrays
    i = j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p, r):
    """
    This function sorts the array A[p..r] using the merge sort algorithm.
    """
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        # Test with a simple list
        a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        merge_sort(a, 0, len(a) - 1)
        self.assertEqual(a, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

        # Test with an already sorted list
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        merge_sort(b, 0, len(b) - 1)
        self.assertEqual(b, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        # Test with a list sorted in reverse order
        c = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        merge_sort(c, 0, len(c) - 1)
        self.assertEqual(c, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()
