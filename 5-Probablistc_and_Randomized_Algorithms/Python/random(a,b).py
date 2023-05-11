import random
import math
import unittest

# Author: Robert Joseph

def pow2(p):
    """
    This function generates a random integer with p bits using the
    Horner's rule with base 2.
    """
    r = 0
    for i in range(p):
        r = 2 * r + random.randint(0, 1)
    return r

def random1(a, b):
    """
    This function generates a random integer between a and b inclusive,
    using the binary representation of the random number and the Horner's
    rule with base 2.
    Time complexity: O(log(b-a)).
    Reference: https://stackoverflow.com/questions/8692818/how-to-implement-randoma-b-with-only-random0-1
    """
    # compute the number of bits needed to represent the range [a, b]
    p = math.ceil(math.log2(b - a + 1))
    
    # generate random numbers until a valid number is obtained
    while True:
        r = pow2(p)
        if r > a + b:
            continue
        else:
            return a + r


class TestRandom1(unittest.TestCase):
    def test_random1(self):
        # Test with a = 0, b = 99
        a = 0
        b = 99
        for i in range(1000):
            x = random1(a, b)
            self.assertGreaterEqual(x, a)
            self.assertLessEqual(x, b)

        # Test with a = -10, b = 10
        a = -10
        b = 10
        for i in range(1000):
            x = random1(a, b)
            self.assertGreaterEqual(x, a)
            self.assertLessEqual(x, b)

        # Test with a = 100, b = 200
        a = 100
        b = 200
        for i in range(1000):
            x = random1(a, b)
            self.assertGreaterEqual(x, a)
            self.assertLessEqual(x, b)


if __name__ == '__main__':
    unittest.main()
