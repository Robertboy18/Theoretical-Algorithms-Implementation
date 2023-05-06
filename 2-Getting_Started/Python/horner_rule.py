import unittest

# Author: Robert Joseph

def horner_rule(a, n, x):
    """
    This function implements the Horner's rule for evaluating a polynomial
    of degree n with coefficients a[0], a[1], ..., a[n-1] at the point x.
    """
    # initialize y with the constant term of the polynomial
    y = a[0]
    
    # iterate over the remaining terms of the polynomial
    for i in range(1, n):
        # update y by adding the next coefficient and multiplying by x
        y = a[i] + x*y
    
    # return the final result
    return y


class TestHornerRule(unittest.TestCase):
    def test_horner_rule(self):
        # Test with polynomial f(x) = 2x^2 + 3x + 4
        a = [4, 3, 2][::-1]
        n = len(a)
        x = 5
        self.assertEqual(horner_rule(a, n, x), 69)

        # Test with polynomial f(x) = x^3 + 2x^2 + 3x + 4
        a = [4, 3, 2, 1][::-1]
        n = len(a)
        x = 5
        self.assertEqual(horner_rule(a, n, x), 194)

        # Test with polynomial f(x) = 1
        a = [1][::-1]
        n = len(a)
        x = 5
        self.assertEqual(horner_rule(a, n, x), 1)


if __name__ == '__main__':
    unittest.main()
