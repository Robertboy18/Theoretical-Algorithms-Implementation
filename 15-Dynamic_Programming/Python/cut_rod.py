import sys
import unittest

# Author: Robert Joseph

def cutRod(arr, n):
    """
    This function calculates the maximum obtainable value by cutting a rod
    of length n given the price of each possible piece.
    
    Time Complexity: O(2^n)
    """
    if n == 0:
        return 0
    q = -sys.maxsize
    for i in range(n):
        q = max(q, arr[i] + cutRod(arr, n-i-1))
    return q

def memoized_cut(arr, n):
    """
    This function calculates the maximum obtainable value using memoization,
    which is a top-down approach.
    
    Time Complexity: O(n^2)
    """
    r = [-sys.maxsize for _ in range(n)]
    return cutRod_memoized(arr, n, r)

def cutRod_memoized(arr, n, r):
    if r[n-1] >= 0:
        return r[n-1]
    if n == 0:
        q = 0
    else:
        q = -sys.maxsize
        for i in range(1, n):
            q = max(q, arr[i] + cutRod_memoized(arr, n-i-1, r))
    r[n-1] = q
    return q

def bottom_up_cut_rod(arr, n):
    """
    This function calculates the maximum obtainable value using a bottom-up
    dynamic programming approach.
    
    Time Complexity: O(n^2)
    """
    r = [0] * (n+1)
    for i in range(1, n+1):
        q = -sys.maxsize
        for j in range(i):
            q = max(q, arr[j] + r[i-j-1])
        r[i] = q
    return r[n]


class TestCutRod(unittest.TestCase):
    def test_cutRod(self):
        arr = [1, 5, 8]
        n = len(arr)
        self.assertEqual(cutRod(arr, n), 8)

    def test_memoized_cut(self):
        arr = [1, 5, 8]
        n = len(arr)
        self.assertEqual(memoized_cut(arr, n), 8)

    def test_bottom_up_cut_rod(self):
        arr = [1, 5, 8]
        n = len(arr)
        self.assertEqual(bottom_up_cut_rod(arr, n), 8)


if __name__ == '__main__':
    unittest.main()
