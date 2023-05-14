import unittest

# Author: Robert Joseph

def plusOne(A):
    """
    This function takes a non-negative integer represented as an array of digits
    and returns the integer plus one in the same format.
    
    The time complexity of this function is O(n), where n is the length of the input array A. This is because the function iterates over each digit in the array at most once.
    """
    carry = 1
    for i in range(len(A)-1, -1, -1):
        A[i] += carry
        carry = A[i] // 10
        A[i] %= 10

    if carry:
        A.insert(0, 1)

    return A


class TestPlusOne(unittest.TestCase):
    def test_plus_one(self):
        # test with input [0, 0, 1]
        A = [0, 0, 1]
        self.assertEqual(plusOne(A), [0, 0, 2])

        # test with input [1, 2, 3]
        A = [1, 2, 3]
        self.assertEqual(plusOne(A), [1, 2, 4])

        # test with input [9, 9, 9]
        A = [9, 9, 9]
        self.assertEqual(plusOne(A), [1, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
