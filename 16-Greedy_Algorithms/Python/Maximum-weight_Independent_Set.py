#Let X be a finite set of elements with two partitions A, B (figure 1(a)). Each element x ∈ X has weight w(x).
#Also, we are given three values bA, bB, bX ∈ Z≥0. We wish to find the maximum weight subset Y ⊆ X such that
#1. |Y | ≤ bX,
#2. |Y ∩ A| ≤ bA, and
#3. |Y ∩ B| ≤ bB,
#where weight of Y is equal to sum i∈Y w(x).

import unittest

# Author: Robert Joseph

def maximum(X, weights, A, B, bA, bB, bX):
    """
    This function finds the maximum weight subset Y from the set X, given the weights of the elements,
    and the constraints on the subsets Y ∩ A, Y ∩ B, and Y.
    """
    Y = []
    X = [x for _, x in sorted(zip(weights, X))]  # Sort X based on weights
    for i in range(len(X)):
        # Add the next element from X to Y
        Y.append(X[i])
        
        # Calculate the sizes of Y, Y ∩ A, and Y ∩ B
        value1 = len(Y)
        value2 = len(list(set(Y) & set(A)))
        value3 = len(list(set(Y) & set(B)))
        
        # Check if the current subset Y satisfies the constraints
        if value1 <= bX and value2 <= bA and value3 <= bB:
            pass
        else:
            Y.remove(X[i])
    
    return Y


class TestMaximum(unittest.TestCase):
    def test_maximum(self):
        X = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        A = {1, 2, 3, 4, 5}
        B = {6, 7, 8, 9, 10}
        bA = 12
        bB = 31
        bX = 33
        weights = {2, 3, 3, 4, 5, 6, 7, 8, 9, 10}
        self.assertEqual(maximum(X, weights, A, B, bA, bB, bX), {1, 2, 3, 4, 5, 6, 7, 8, 9, 10})

        # Test with smaller sets and constraints
        X = {1, 2, 3}
        A = {1, 2}
        B = {2, 3}
        bA = 2
        bB = 2
        bX = 3
        weights = {2, 3, 1}
        self.assertEqual(maximum(X, weights, A, B, bA, bB, bX), {1, 2})

        # Test with empty set
        X = set()
        A = {1, 2, 3}
        B = {4, 5, 6}
        bA = 2
        bB = 2
        bX = 3
        weights = set()
        self.assertEqual(maximum(X, weights, A, B, bA, bB, bX), set())


if __name__ == '__main__':
    unittest.main()
