import unittest

# Author: Robert Joseph

def fib1(n):
    """
    This function computes the nth Fibonacci number using a recursive algorithm.
    """
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        # Test with n = 0
        self.assertEqual(fib1(0), 0)

        # Test with n = 5
        self.assertEqual(fib1(5), 5)

        # Test with n = 10
        self.assertEqual(fib1(10), 55)


if __name__ == '__main__':
    unittest.main()
