import math
import unittest

# Author: Robert Joseph

def count_inversions(A, p, r):
    """
    This function counts the number of inversions in an array A[p..r]
    using the merge sort algorithm.
    """
    if p < r:
        # split the array in half and recursively count inversions
        q = math.floor((p + r) / 2)
        left = count_inversions(A, p, q)
        right = count_inversions(A, q + 1, r)
        if left == None:
            left = 0
        if right == None:
            right = 0
        # merge the two sorted halves and count split inversions
        inversions = merge_inversions(A, p, q, r) + left + right
        return inversions


def merge_inversions(A, p, q, r):
    """
    This function merges two sorted subarrays A[p..q] and A[q+1..r]
    and counts the number of split inversions.
    """
    n1 = q - p + 1
    n2 = r - q
    L,R = [0]*(n1+1),[0]*(n2+1)
    for i in range(0,n1):
        L[i] = A[p + i]
    for j in range(0,n2):
        R[j] = A[q + j + 1]
    L[n1] = math.inf
    R[n2] = math.inf
    i = 0
    j = 0
    inversions = 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            inversions = inversions + n1 - i
            A[k] = R[j]
            j = j + 1
    return inversions


class TestCountInversions(unittest.TestCase):
    def test_count_inversions(self):
        # Test with array [1, 3, 5, 2, 4, 6]
        A = [1, 3, 5, 2, 4, 6]
        p = 0
        r = len(A) - 1
        self.assertEqual(count_inversions(A, p, r), 3)

        # Test with array [2, 4, 6, 1, 3, 5]
        A = [2, 4, 6, 1, 3, 5]
        p = 0
        r = len(A) - 1
        self.assertEqual(count_inversions(A, p, r), 6)

        # Test with array [1, 2, 3, 4, 5, 6]
        A = [1, 2, 3, 4, 5, 6]
        p = 0
        r = len(A) - 1
        self.assertEqual(count_inversions(A, p, r), 0)


if __name__ == '__main__':
    unittest.main()
