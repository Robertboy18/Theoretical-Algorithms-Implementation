import unittest

# Author: Robert Joseph

def matrix_partition(A, n1, k, l):
    """
    This function partitions the input matrix A into an n1 x n1 submatrix
    starting at position (k, l).
    """
    A1 = []
    for i in range(k, k+n1):
        row = []
        for j in range(l, l+n1):
            row.append(A[i][j])
        A1.append(row)
    return A1


def matrix_multiply_divide(A, B):
    """
    This function multiplies two matrices A and B using the divide-and-conquer algorithm.
    """
    # time complexity: O(n^3), where n is the dimension of the input matrices

    # create a new matrix C to store the result
    C = [[0 for __ in range(len(B[0]))] for j in range(len(A))]

    # base case: if the matrices are both 1x1, compute the product and return it
    if len(A) == 1 and len(B) == 1:
        return [[A[0][0] * B[0][0]]]

    # otherwise, partition the matrices into smaller submatrices and recursively compute their product
    else:
        # determine the size of the submatrices
        n = len(A)
        n1 = n // 2

        # partition the matrices into submatrices
        A11 = matrix_partition(A, n1, 0, 0)
        A12 = matrix_partition(A, n1, 0, n1)
        A21 = matrix_partition(A, n1, n1, 0)
        A22 = matrix_partition(A, n1, n1, n1)
        B11 = matrix_partition(B, n1, 0, 0)
        B12 = matrix_partition(B, n1, 0, n1)
        B21 = matrix_partition(B, n1, n1, 0)
        B22 = matrix_partition(B, n1, n1, n1)

        # recursively compute the product of the submatrices
        C11 = matrix_multiply_divide(A11, B11) + matrix_multiply_divide(A12, B21)
        C12 = matrix_multiply_divide(A11, B12) + matrix_multiply_divide(A12, B22)
        C21 = matrix_multiply_divide(A21, B11) + matrix_multiply_divide(A22, B21)
        C22 = matrix_multiply_divide(A21, B12) + matrix_multiply_divide(A22, B22)

        # combine the submatrices into the final result
        for i in range(n1):
            for j in range(n1):
                C[i][j] = C11[i][j]
                C[i][j+n1] = C12[i][j]
                C[i+n1][j] = C21[i][j]
                C[i+n1][j+n1] = C22[i][j]

        return C

class TestMatrixMultiply(unittest.TestCase):
    def test_matrix_multiply(self):
        # test with 2x2 matrices
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiply_divide(A, B), expected_result)

        # test with 3x3 matrices
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        expected_result = [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
        self.assertEqual(matrix_multiply_divide(A, B), expected_result)
        
        # test with 4x4 matrices
        A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [4, 5, 6, 7]]
        B = [[7, 8, 9, 1], [2, 3, 4, 5], [6, 7, 8, 9], [1, 2, 3, 4]]
        expected_result = [[40, 50, 60, 40], [104, 130, 156, 104], [40, 50, 60, 40], [104, 130, 156, 104]]
        self.assertEqual(matrix_multiply_divide(A, B), expected_result)
        
if __name__ == '__main__':
    unittest.main()

