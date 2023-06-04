import unittest

# Author: Robert Joseph

def binomial_recursive(n, k):
    """
    This function calculates the binomial coefficient C(n, k) using a recursive approach.
    Time Complexity: O(2^n)
    """
    if n == 0:
        return 0
    else:
        if k == 0 or k == n:
            return 1
        else:
            return binomial_recursive(n-1, k-1) + binomial_recursive(n-1, k)

soln = [[-1 for i in range(k)] for i in range(n)]

def binomial_memoized(n, k):
    """
    This function calculates the binomial coefficient C(n, k) using a memoized approach.
    Time Complexity: O(n*k)
    Space Complexity: O(n*k)
    """
    if soln[n-1][k-1] > -1:
        return soln[n-1][k-1]
    if k == 0 or k == n:
        return 1
    else:
        soln[n-1][k-1] = binomial_memoized(n-1, k-1) + binomial_memoized(n-1, k)
        return soln[n-1][k-1]

def binomial_iterative(n, r):
    """
    This function calculates the binomial coefficient C(n, r) using an iterative approach.
    Time Complexity: O(n*r)
    Space Complexity: O(r)
    """
    if n < r:
        return 0
    if (n - r) < r:
        r = n - r
    dp = [0] * (r + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, r), 0, -1):
            dp[j] += dp[j - 1]
    return dp[r]

class TestBinomial(unittest.TestCase):
    def test_binomial_recursive(self):
        self.assertEqual(binomial_recursive(5, 3), 10)

    def test_binomial_memoized(self):
        self.assertEqual(binomial_memoized(5, 3), 10)

    def test_binomial_iterative(self):
        self.assertEqual(binomial_iterative(5, 3), 10)

if __name__ == '__main__':
    unittest.main()
