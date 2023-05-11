import random
import unittest

# Author: Robert Joseph

def morris_counter(bits):
    """
    The Morris counter algorithm is a randomized algorithm for counting a large number of events using a small amount of memory.
    Invented in 1977 by Robert Morris of Bell Labs, it uses probabilistic techniques to increment the counter.
    
    Here, we increment count with a probability of 1/2 to the power of count and we return 2 to the power of count minus 1.
    """
    count = 0
    while True:
        if count < 2**bits - 1:
            prob = random.random()
            if prob < 1 / (2**count):
                count += 1
        else:
            break
    return 2**count - 1

class TestMorrisCounter(unittest.TestCase):
    def test_small_counter(self):
        # Test the counter for a small value of bits
        bits = 4
        self.assertEqual(morris_counter(bits), 7)

    def test_large_counter(self):
        # Test the counter for a large value of bits
        bits = 100
        self.assertTrue(morris_counter(bits) >= 2**bits * 0.9)

    def test_zero_bits(self):
        # Test the counter for zero bits
        bits = 0
        self.assertEqual(morris_counter(bits), 0)

if __name__ == '__main__':
    unittest.main()
