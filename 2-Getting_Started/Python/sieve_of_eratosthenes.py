import unittest

# Author: Robert Joseph

def sieve(n):
    """
    This function implements the Sieve of Eratosthenes algorithm to find all
    prime numbers up to n.
    """
    k = []
    primes = []
    # iterate over all numbers from 2 to n
    for i in range(2, n+1):
        # if i has not been marked as composite (i.e., not in k), it is prime
        if i not in k:
            # print i as a prime number
            primes.append(i)
            # mark all multiples of i as composite
            for j in range(i*i, n+1, i):
                k.append(j)
                
    # return the list of composite numbers and primes
    return k, primes


class TestSieve(unittest.TestCase):
    # enough to test the composite numbers
    def test_sieve(self):
        # Test with n = 10
        self.assertEqual(sorted(sieve(10)[0]), [4, 6, 8, 9, 10])

        # Test with n = 20
        self.assertEqual(sorted(sieve(20)[0]), [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20])

        # Test with n = 30
        self.assertEqual(sorted(sieve(30)[0]), [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30])


if __name__ == '__main__':
    unittest.main()
