import unittest

# Author: Robert Joseph

def strassen(matrix_a, matrix_b):
    """
    This function implements the Strassen's algorithm for matrix multiplication.
    It has a time complexity of O(N^2.78), which is faster than the standard
    matrix multiplication algorithm that has a time complexity of O(N^3).
    """
    # check if matrices have the same dimensions
    if get_matrix_dimensions(matrix_a) != get_matrix_dimensions(matrix_b):
        raise Exception(f'Both matrices are not the same dimension! \nMatrix A:{matrix_a} \nMatrix B:{matrix_b}')

    # base case: if matrices are 2x2, use default matrix multiplication
    if get_matrix_dimensions(matrix_a) == (2, 2):
        return default_matrix_multiplication(matrix_a, matrix_b)

    # split matrices into 4 submatrices
    A, B, C, D = split_matrix(matrix_a)
    E, F, G, H = split_matrix(matrix_b)

    # calculate 7 products using recursive calls to the Strassen's algorithm
    p1 = strassen(A, matrix_subtraction(F, H))
    p2 = strassen(matrix_addition(A, B), H)
    p3 = strassen(matrix_addition(C, D), E)
    p4 = strassen(D, matrix_subtraction(G, E))
    p5 = strassen(matrix_addition(A, D), matrix_addition(E, H))
    p6 = strassen(matrix_subtraction(B, D), matrix_addition(G, H))
    p7 = strassen(matrix_subtraction(A, C), matrix_addition(E, F))

    # combine the 7 products into the final result
    top_left = matrix_addition(matrix_subtraction(matrix_addition(p5, p4), p2), p6)
    top_right = matrix_addition(p1, p2)
    bot_left = matrix_addition(p3, p4)
    bot_right = matrix_subtraction(matrix_subtraction(matrix_addition(p1, p5), p3), p7)
    new_matrix = []
    for i in range(len(top_right)):
        new_matrix.append(top_left[i] + top_right[i])
    for i in range(len(bot_right)):
        new_matrix.append(bot_left[i] + bot_right[i])
    return new_matrix


class TestStrassen(unittest.TestCase):
    def test_strassen(self):
        # Test with 2x2 matrices
        matrix_a = [[1, 2], [3, 4]]
        matrix_b = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]
        self.assertEqual(strassen(matrix_a, matrix_b), expected_result)

        # Test with 3x3 matrices
        matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        expected_result = [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
        self.assertEqual(strassen(matrix_a, matrix_b), expected_result)

        # Test with 4x4 matrices
        matrix_a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        matrix_a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        expected_result = [[90, 100, 110, 120], [202, 228, 254, 280], [314, 356, 398, 440], [426, 484, 542, 600]]
        self.assertEqual(strassen(matrix_a, matrix_b), expected_result)
        
if __name__ == '__main__':
    unittest.main()
