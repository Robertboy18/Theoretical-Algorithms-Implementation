import unittest

# Author: Robert Joseph

def matrix_partition(A, n1, k, l):
    """
    This function partitions the input matrix A into an n1 x n1 submatrix
    starting at position (k, l).
    """
    A1 = []
    for i in range(k, n1 + k):
        row = []
        for j in range(l, n1 + l):
            row.append(A[i][j])
        A1.append(row)
    return A1


def matrix_multiply_divide(A, B):
    """
    This function multiplies two matrices A and B using the divide-and-conquer algorithm.
    """
    # time complexity: O(n^3), where n is the dimension of the input matrices

    # create a new matrix C to store the result
    C = [[0 for __ in range(len(A))] for j in range(len(A))]

    # base case: if the matrices are both 1x1, compute the product and return it
    if len(A) == 1:
        return A[0][0] * B[0][0]

    # otherwise, partition the matrices into smaller submatrices and recursively compute their product
    else:
        # determine the size of the submatrices
        n1 = len(A) // 2

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
        C = [[C11, C12], [C21, C22]]

        return C
    
def default_matrix_multiplication(a, b):
    """
    Only for 2x2 matrices
    """
    if len(a) != 2 or len(a[0]) != 2 or len(b) != 2 or len(b[0]) != 2:
        raise Exception('Matrices should be 2x2!')
    print(a[0][0] * b[0][1] + a[0][1] * b[1][1])
    new_matrix = [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                  [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

    return new_matrix


def matrix_addition(matrix_a, matrix_b):
    # print(matrix_a)
    return [[matrix_a[row][col] + matrix_b[row][col]
             for col in range(len(matrix_a[row]))] for row in range(len(matrix_a))]


def matrix_subtraction(matrix_a, matrix_b):
    return [[matrix_a[row][col] - matrix_b[row][col]
             for col in range(len(matrix_a[row]))] for row in range(len(matrix_a))]


def split_matrix(a):
    """
    Given a matrix, return the TOP_LEFT, TOP_RIGHT, BOT_LEFT and BOT_RIGHT quadrant
    """
    if len(a) % 2 != 0 or len(a[0]) % 2 != 0:
        raise Exception('Odd matrices are not supported!')

    matrix_length = len(a)
    mid = matrix_length // 2
    top_left = [[a[i][j] for j in range(mid)] for i in range(mid)]
    bot_left = [[a[i][j] for j in range(mid)] for i in range(mid, matrix_length)]

    top_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid)]
    bot_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid, matrix_length)]

    return top_left, top_right, bot_left, bot_right


def get_matrix_dimensions(matrix):
    return len(matrix), len(matrix[0])


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

