import random
import unittest

# Author: Robert Joseph

def random_search(A, element):
    """
    This function performs a randomized search in the array A for the
    given element. The search stops after n iterations, where n is the
    length of A. The expected running time is O(n).
    """
    # initialize the checked list to False for all indices
    checked = [False] * len(A)
    
    # iterate until we have checked all indices
    j = 0
    while j < len(A):
        # choose a random index i that hasn't been checked yet
        i = random.randint(0, len(A) - 1)
        if not checked[i]:
            checked[i] = True
            j += 1
        # if we find the element, return its index
        if A[i] == element:
            return i
    
    # if we haven't found the element after n iterations, return -1
    return -1


class TestRandomSearch(unittest.TestCase):
    def test_random_search(self):
        # test with an array of even length
        A = [1, 2, 3, 4, 5, 6]
        self.assertIn(random_search(A, 3), range(len(A)))
        self.assertIn(random_search(A, 7), [-1])

        # test with an array of odd length
        A = [1, 2, 3, 4, 5]
        self.assertIn(random_search(A, 4), range(len(A)))
        self.assertIn(random_search(A, 6), [-1])

        # test with an empty array
        A = []
        self.assertEqual(random_search(A, 1), -1)


if __name__ == '__main__':
    unittest.main()
