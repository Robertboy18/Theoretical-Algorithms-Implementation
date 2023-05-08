import unittest

# Author: Robert Joseph

def matrix_multiply(A, B):
    """
    This function performs matrix multiplication between two matrices A and B.
    The time complexity of this function is O(n^3), where n is the size of the matrices.
    """
    if len(A) != len(B):
        return False
    else:
        n = len(A)
        C = [[0 for __ in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                C[i][j] = 0
                for k in range(n):
                    C[i][j] += A[i][k] * B[k][j]
        return C


class TestMatrixMultiply(unittest.TestCase):
    def test_matrix_multiply(self):
        # Test with 2x2 matrices
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiply(A, B), expected_result)

        # Test with 3x3 matrices
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        expected_result = [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
        self.assertEqual(matrix_multiply(A, B), expected_result)

        # Test with non-square matrices
        A = [[1, 2, 3], [4, 5, 6]]
        B = [[7, 8], [9, 10], [11, 12]]
        expected_result = [[58, 64], [139, 154]]
        self.assertEqual(matrix_multiply(A, B), expected_result)


if __name__ == '__main__':
    unittest.main()
