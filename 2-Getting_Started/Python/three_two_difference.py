import unittest

# Author: Robert Joseph

def three_two(n):
    """
    This function calculates the value of the expression 3^n - 2^n
    using a recursive algorithm based on the recurrence relation:
    
        T(n) = 5*T(n-1) - 6*T(n-2)
    
    with initial values T(0) = 0 and T(1) = 1.
    """
    # base cases
    if n <= 1:
        return n
    
    # recursive cases
    else:
        return 5*three_two(n-1) - 6*three_two(n-2)


class TestThreeTwo(unittest.TestCase):
    def test_three_two(self):
        self.assertEqual(three_two(0), 0)
        self.assertEqual(three_two(1), 1)
        self.assertEqual(three_two(10), 295245)


if __name__ == '__main__':
    unittest.main()
