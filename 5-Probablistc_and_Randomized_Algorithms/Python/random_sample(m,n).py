import random
import unittest

# Author: Robert Joseph

def random_sample_standard(m, n):
    """
    This function generates a random sample of m elements from the range [0, n-1]
    using the standard shuffle algorithm. The expected running time is O(m*n).
    """
    # initialize a list with elements from 0 to n-1
    A = [i for i in range(n)]
    # shuffle the list randomly
    random.shuffle(A)
    # return the first m elements of the shuffled list
    return A[:m]


def random_sample(m, n):
    """
    This function generates a random sample of m elements from the range [0, n-1]
    using recursive selection. The expected running time is O(m).
    """
    # base case: if m is 0, return an empty list
    if m == 0:
        return []
    else:
        # recursively generate a sample of size m-1 from the range [0, n-2]
        S = random_sample(m-1, n-1)
        # generate a random integer i from 0 to n-1
        i = random.randint(0, n-1)
        # if i is already in the sample S, append n-1 to S
        if i in S:
            S.append(n-1)
        # otherwise, append i to S
        else:
            S.append(i)
        # return the resulting sample
        return S


class TestRandomSample(unittest.TestCase):
    def test_random_sample_standard(self):
        # test with m = 5, n = 10
        m = 5
        n = 10
        sample = random_sample_standard(m, n)
        self.assertEqual(len(sample), m)
        self.assertCountEqual(sample, range(n))

    def test_random_sample(self):
        # test with m = 5, n = 10
        m = 5
        n = 10
        sample = random_sample(m, n)
        self.assertEqual(len(sample), m)
        self.assertCountEqual(sample, range(n))

    def test_random_sample_with_duplicates(self):
        # test with m = 5, n = 5 (the range has only 5 elements)
        m = 5
        n = 5
        sample = random_sample(m, n)
        self.assertEqual(len(sample), m)
        self.assertCountEqual(sample, range(n))


if __name__ == '__main__':
    unittest.main()
