import unittest

# Author: Robert Joseph

def monge(A):
    """
    This function checks whether a given matrix A satisfies the Monge property,
    which is defined as follows:
    
    For all i < k < m and j < l < n, the following inequality holds:
    A[i][j] + A[k][l] <= A[i][l] + A[k][j]
    """
    m = len(A)
    n = len(A[0])
    for i in range(m-1):
        for j in range(n-1):
            # check the Monge property for the current 2x2 submatrix
            if A[i][j] + A[i+1][j+1] > A[i][j+1] + A[i+1][j]:
                return False
    return True

class TestMonge(unittest.TestCase):
    def test_monge_true(self):
        # Test with a matrix that satisfies the Monge property
        A = [[10, 17, 13, 28, 23],
             [17, 22, 16, 29, 23],
             [24, 28, 22, 34, 24],
             [11, 13, 6, 17, 7],
             [45, 44, 32, 37, 23]]
        self.assertTrue(monge(A))

    def test_monge_false(self):
        # Test with a matrix that does not satisfy the Monge property
        A = [[10, 17, 13],
             [17, 22, 16],
             [24, 28, 22],
             [11, 13, 6]]
        self.assertFalse(monge(A))

    def test_monge_single_row(self):
        # Test with a matrix that has only one row
        A = [[10, 17, 13, 28, 23]]
        self.assertTrue(monge(A))

if __name__ == '__main__':
    unittest.main()
