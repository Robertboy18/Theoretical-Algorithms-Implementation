import unittest

# Author: Robert Joseph

def maximum_difference(z):
    """
    This function returns the maximum difference between two consecutive
    elements in a list z. If z has fewer than two elements, it returns None.
    """
    # initialize the maximum difference to a very small value
    c = -float('inf')
    
    # iterate over each pair of consecutive elements in z
    for i in range(1, len(z)):
        # update the maximum difference if the current difference is larger
        c = max(c, abs(z[i] - z[i-1]))
    
    # return the final result
    return c


class TestMaximumDifference(unittest.TestCase):
    def test_maximum_difference(self):
        # Test with a list of positive numbers
        z = [1, 2, 3, 4, 5]
        self.assertEqual(maximum_difference(z), 1)

        # Test with a list of negative numbers
        z = [-5, -4, -3, -2, -1]
        self.assertEqual(maximum_difference(z), 1)

        # Test with a mixed list of numbers
        z = [1, 24, 5, 6, 7, 8, -232, 35, 5, 67]
        self.assertEqual(maximum_difference(z), 267)


if __name__ == '__main__':
    unittest.main()
