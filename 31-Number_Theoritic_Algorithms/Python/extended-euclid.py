import unittest

# Author: Robert Joseph

def extended_euclid(a, b):
    """
    This function calculates the greatest common divisor (GCD) of two numbers
    'a' and 'b' using the extended Euclidean algorithm. It also returns the
    coefficients 'x' and 'y' such that ax + by = gcd(a, b).
    """
    if b == 0:
        # Base case: if b is zero, the GCD is a, and x and y are 1 and 0 respectively
        return (a, 1, 0)
    else:
        # Recursive case: calculate GCD, x, and y using the extended Euclidean algorithm
        (g, x, y) = extended_euclid(b, a % b)
        return (g, y, x - (a // b) * y)

class TestExtendedEuclid(unittest.TestCase):
    def test_extended_euclid(self):
        # Test with numbers 99 and 78
        a = 99
        b = 78
        (g, x, y) = extended_euclid(a, b)
        self.assertEqual(g, 3)  # GCD of 99 and 78 is 3
        self.assertEqual(x, -11)  # x coefficient: -11
        self.assertEqual(y, 14)  # y coefficient: 14

        # Test with numbers 100 and 17
        a = 100
        b = 17
        (g, x, y) = extended_euclid(a, b)
        self.assertEqual(g, 1)  # GCD of 100 and 17 is 1
        self.assertEqual(x, 7)  # x coefficient: 7
        self.assertEqual(y, -41)  # y coefficient: -41

        # Test with numbers 252 and 198
        a = 252
        b = 198
        (g, x, y) = extended_euclid(a, b)
        self.assertEqual(g, 18)  # GCD of 252 and 198 is 18
        self.assertEqual(x, -5)  # x coefficient: -5
        self.assertEqual(y, 6)  # y coefficient: 6

if __name__ == '__main__':
    unittest.main()
