import unittest

# Author: Robert Joseph

def linear_search(x, m):
    """
    This function searches for an element m in the list x using linear search,
    and returns the index of the first occurrence of m in x if found, or "NIL" otherwise.
    """
    # iterate over the elements of x
    for i in range(len(x)):
        # if the current element is equal to m, return its index
        if x[i] == m:
            return i
    
    # if m is not found in x, return "NIL"
    return "NIL"


class TestLinearSearch(unittest.TestCase):
    def test_linear_search(self):
        # Test with a list containing the element
        x = [1, 2, 3, 4, 5]
        m = 3
        self.assertEqual(linear_search(x, m), 2)

        # Test with a list not containing the element
        x = [1, 2, 3, 4, 5]
        m = 6
        self.assertEqual(linear_search(x, m), "NIL")

        # Test with an empty list
        x = []
        m = 5
        self.assertEqual(linear_search(x, m), "NIL")


if __name__ == '__main__':
    unittest.main()
