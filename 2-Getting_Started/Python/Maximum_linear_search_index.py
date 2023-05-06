import unittest

# Author: Robert Joseph

def max_linear_search_index(n, m):
    """
    This function performs a linear search for the maximum index of an element
    in a list that matches a given value. If no match is found, returns "NIL".
    """
    # initialize the maximum index to -1
    c = -1
    
    # iterate over the list
    for i in range(len(n)):
        # if the current element matches the given value, update the maximum index
        if n[i] == m:
            c = max(c, i)
    
    # if no match was found, return "NIL"; otherwise, return the maximum index
    if c == -1:
        return "NIL"
    else:
        return c


class TestMaxLinearSearchIndex(unittest.TestCase):
    def test_max_linear_search_index(self):
        # Test with a list containing multiple occurrences of the target value
        n = [1, 2, 34, 23, 44, 44, 44, 44, 4453]
        m = 44
        self.assertEqual(max_linear_search_index(n, m), 7)

        # Test with a list containing a single occurrence of the target value
        n = [1, 2, 34, 23, 44, 12, 9]
        m = 44
        self.assertEqual(max_linear_search_index(n, m), 4)

        # Test with a list that doesn't contain the target value
        n = [1, 2, 3, 4, 5, 6, 7]
        m = 8
        self.assertEqual(max_linear_search_index(n, m), "NIL")


if __name__ == '__main__':
    unittest.main()
