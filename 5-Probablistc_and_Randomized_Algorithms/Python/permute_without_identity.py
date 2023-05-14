import random
import unittest

# Author: Robert Joseph

def permute_without_identity(A):
    """
    This function takes a list A and returns a random permutation of the
    elements of A, except for the identity permutation.
    """
    n = len(A)
    
    # iterate over the first n-1 elements of A
    for i in range(n - 1):
        # choose a random index j such that i < j < n
        j = random.randint(i + 1, n - 1)
        # swap A[i] and A[j]
        A[i], A[j] = A[j], A[i]
    
    # return the shuffled list
    return A


class TestPermuteWithoutIdentity(unittest.TestCase):
    def test_permute_without_identity(self):
        # Test with a list of length 3
        A = [1, 2, 3]
        B = permute_without_identity(A)
        self.assertNotEqual(B, A)
        self.assertCountEqual(B, A)

        # Test with a list of length 5
        A = [1, 2, 3, 4, 5]
        B = permute_without_identity(A)
        self.assertNotEqual(B, A)
        self.assertCountEqual(B, A)

        # Test with a list of length 1
        A = [1]
        B = permute_without_identity(A)
        self.assertEqual(B, A)


if __name__ == '__main__':
    unittest.main()
