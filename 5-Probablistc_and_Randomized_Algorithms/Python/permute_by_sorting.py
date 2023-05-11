import random
import math
import unittest

# Author: Robert Joseph

def permute_by_sorting_v2(A):
    """
    This function shuffles the input list A by first generating a random priority
    value for each element in A and then sorting the elements based on their priority.
    The time complexity of this algorithm is O(n log n), where n is the length of A.
    """
    n = len(A)
    P = [0] * n
    
    # generate a random priority value for each element in A
    for i in range(n):
        P[i] = random.randint(0, n**3)
    
    # sort the elements in A based on their priority values
    A = [A[i] for i in sorted(range(n), key=lambda i: P[i])]
    return A


class TestPermuteBySorting(unittest.TestCase):
    def test_permute_by_sorting_v2(self):
        # Test with list of even length
        A = [1,2,3,4,5,6]
        self.assertNotEqual(permute_by_sorting_v2(A), A)
        self.assertEqual(set(permute_by_sorting_v2(A)), set(A))

        # Test with list of odd length
        A = [1,2,3,4,5,6,7]
        self.assertNotEqual(permute_by_sorting_v2(A), A)
        self.assertEqual(set(permute_by_sorting_v2(A)), set(A))

        # Test with list of length 1
        A = [1]
        self.assertEqual(permute_by_sorting_v2(A), A)


if __name__ == '__main__':
    unittest.main()
