import unittest

# Author: Robert Joseph

def sum_n_cubes(n):
    """
    This function calculates the sum of the cubes of the first n positive integers.
    """
    # Base case: if n is 1 or less, return n
    if n <= 1:
        return n
    # Recursive case: sum the cubes of the first n-1 integers and add the cube of n
    else:
        return sum_n_cubes(n-1) + n**3

class TestSumNCubes(unittest.TestCase):
    def test_sum_n_cubes(self):
        # Test with n = 1
        self.assertEqual(sum_n_cubes(1), 1)

        # Test with n = 2
        self.assertEqual(sum_n_cubes(2), 9)

        # Test with n = 10
        self.assertEqual(sum_n_cubes(10), 3025)


if __name__ == '__main__':
    unittest.main()
