import numpy as np
import unittest

# Author: Robert Joseph

def biased_random(p):
    """
    This function returns 1 with probability p and 0 with probability (1-p).
    """
    return np.random.binomial(1, p)

def biased(p):
    """
    This function generates a biased coin toss with probability of heads p.
    """
    # The expected value of x is p(1-p).
    # The expected value of y is p(1-p).
    # Therefore, the expected value of 1 is (1-2p(1-p))/(2p(1-p)).
    while True:
        x = biased_random(p)
        y = biased_random(p)
        if x > y:
            return 1
        else:
            return 0

class TestBiasedCoin(unittest.TestCase):
    def test_biased_coin(self):
        # Test with p = 0.2
        p = 0.2
        num_trials = 10000
        num_heads = sum([biased(p) for i in range(num_trials)])
        empirical_prob = num_heads / num_trials
        self.assertAlmostEqual(empirical_prob, p, delta=0.05)

        # Test with p = 0.5
        p = 0.5
        num_trials = 10000
        num_heads = sum([biased(p) for i in range(num_trials)])
        empirical_prob = num_heads / num_trials
        self.assertAlmostEqual(empirical_prob, p, delta=0.05)

        # Test with p = 0.9
        p = 0.9
        num_trials = 10000
        num_heads = sum([biased(p) for i in range(num_trials)])
        empirical_prob = num_heads / num_trials
        self.assertAlmostEqual(empirical_prob, p, delta=0.05)


if __name__ == '__main__':
    unittest.main()
