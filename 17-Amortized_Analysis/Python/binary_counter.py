import unittest

# Author: Robert Joseph

def binary_counter(A):
    """
    This function counts the number of 1s in a binary number.
    """
    count = 0
    while A > 0:
        if A % 2 == 1:
            count += 1
        A = A // 2
    return count


def increment(A):
    """
    This function increments a binary number represented as a list of bits.
    The cost of each increment operation is linear in the number of bits flipped.
    Amortized analysis: Average case is O(1).
    """
    i = 0
    while i < len(A) and A[i] == 1:
        A[i] = 0
        i += 1
    if i < len(A):
        A[i] = 1


class TestBinaryCounter(unittest.TestCase):
    def test_binary_counter(self):
        # Test with binary number 101010
        A = 42
        self.assertEqual(binary_counter(A), 3)

        # Test with binary number 111111
        A = 63
        self.assertEqual(binary_counter(A), 6)

        # Test with binary number 1001
        A = 9
        self.assertEqual(binary_counter(A), 2)


class TestIncrement(unittest.TestCase):
    def test_increment(self):
        # Test incrementing [1, 0, 1, 1]
        A = [1, 0, 1, 1]
        increment(A)
        self.assertEqual(A, [1, 1, 0, 0])

        # Test incrementing [0, 0, 1, 1]
        A = [0, 0, 1, 1]
        increment(A)
        self.assertEqual(A, [0, 1, 0, 0])

        # Test incrementing [1, 1, 1, 1]
        A = [1, 1, 1, 1]
        increment(A)
        self.assertEqual(A, [0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
