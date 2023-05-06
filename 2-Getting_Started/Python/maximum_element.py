import unittest

# Author: Robert Joseph

def maximum(z):
    """
    This function returns the maximum value in a list of numbers z.
    """
    # initialize the current maximum to a very small number
    c = -float('inf')
    
    # iterate over each element in the list
    for i in z:
        # update the current maximum if the current element is larger
        c = max(c, i)
    
    # return the final maximum value
    return c


class TestMaximum(unittest.TestCase):
    def test_maximum(self):
        # Test with a list of positive integers
        z = [1, 2, 3, 4, 5]
        self.assertEqual(maximum(z), 5)

        # Test with a list of negative integers
        z = [-5, -4, -3, -2, -1]
        self.assertEqual(maximum(z), -1)

        # Test with a list that includes zero
        z = [1, 2, 3, 0, -1, -2, -3]
        self.assertEqual(maximum(z), 3)


if __name__ == '__main__':
    unittest.main()
