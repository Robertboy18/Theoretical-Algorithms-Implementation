import unittest

# Author: Robert Joseph

def singleNumber(A):
    """
    This function finds the single number in an array where all other numbers appear twice.
    It uses the bitwise XOR operation to cancel out the duplicate numbers.
    Time complexity: O(N), where N is the length of the array.
    Space complexity: O(1).
    """
    t = 0
    for i in A:
        t = t ^ i
    return t


class TestSingleNumber(unittest.TestCase):
    def test_singleNumber(self):
        # Test with an array containing one single number
        A = [1]
        self.assertEqual(singleNumber(A), 1)

        # Test with an array containing multiple numbers
        A = [1, 2, 3, 2, 3]
        self.assertEqual(singleNumber(A), 1)

        # Test with an array containing negative numbers
        A = [-1, -2, -3, -2, -3]
        self.assertEqual(singleNumber(A), -1)


if __name__ == '__main__':
    unittest.main()
