import random
import unittest

# Author: Robert Joseph

def randomize_in_place(A):
    """
    This function shuffles the input array A in-place using the Fisher-Yates
    algorithm. It selects a random element from the remaining unshuffled
    elements and swaps it with the current element being shuffled.
    """
    # Expected O(N) time complexity, where N is the length of A
    n = len(A)
    for i in range(n):
        j = random.randint(i, n-1) # choose a random index from i to n-1
        A[i], A[j] = A[j], A[i]   # swap the i-th and j-th elements
    return A

class TestRandomizeInPlace(unittest.TestCase):
    def test_randomize_in_place(self):
        # Test with an array of length 1
        A = [1]
        self.assertEqual(randomize_in_place(A), [1])

        # Test with an array of length 2
        A = [1, 2]
        self.assertEqual(sorted(randomize_in_place(A)), [1, 2])

        # Test with an array of length 5
        A = [1, 2, 3, 4, 5]
        self.assertEqual(sorted(randomize_in_place(A)), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
