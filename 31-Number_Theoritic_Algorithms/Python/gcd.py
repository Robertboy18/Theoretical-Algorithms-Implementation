import unittest

# Author: Robert Joseph

def gcd(a, b):
    """
    This function calculates the greatest common divisor (GCD) of two numbers a and b
    using the Euclidean algorithm recursively.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

class TestGCD(unittest.TestCase):
    def test_gcd(self):
        # Test GCD of 12 and 8
        a = 12
        b = 8
        self.assertEqual(gcd(a, b), 4)

        # Test GCD of 24 and 16
        a = 24
        b = 16
        self.assertEqual(gcd(a, b), 8)

        # Test GCD of 81 and 27
        a = 81
        b = 27
        self.assertEqual(gcd(a, b), 27)


if __name__ == '__main__':
    unittest.main()
