def matrix_multiply(A,B):
    # 0(N^3)
    if len(A) != len(B):
        return False
    else:
        C = [[0 for __ in range(len(A))] for j in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A)):
                C[i][j] = 0
                for k in range(len(A)):
                    C[i][j] += A[i][k]*B[k][j]
        return C

def matrix_partition(A,n1,k,l):
    A1 = []
    for i in range(k,n1 + k):
        k = []
        for j in range(l,n1 + l):
            k.append(A[i][j])
        A1.append(k)
    return A1
    
def matrix_multiply_divide(A,B):
    # 0(N^3)
    C = [[0 for __ in range(len(A))] for j in range(len(A))]
    if len(A) == 1:
        return A[0][0]*B[0][0]
    else:
        n1 = len(A)//2
        A11 = matrix_partition(A,n1,0,0)
        A12 = matrix_partition(A,n1,0,n1)
        A21 = matrix_partition(A,n1,n1,0)
        A22 = matrix_partition(A,n1,n1,n1)
        B11 = matrix_partition(B,n1,0,0)
        B12 = matrix_partition(B,n1,0,n1)
        B21 = matrix_partition(B,n1,n1,0)
        B22 = matrix_partition(B,n1,n1,n1)
        
        C11 = matrix_multiply_divide(A11,B11) + matrix_multiply_divide(A12,B21)
        C12 = matrix_multiply_divide(A11,B12) + matrix_multiply_divide(A12,B22)
        C21 = matrix_multiply_divide(A21,B11) + matrix_multiply_divide(A22,B21)
        C22 = matrix_multiply_divide(A21,B12) + matrix_multiply_divide(A22,B22)
        C = [[C11,C22],[C21,C22]]       
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


def strassen(matrix_a, matrix_b):
  # 0(N^{2.78})
    if get_matrix_dimensions(matrix_a) != get_matrix_dimensions(matrix_b):
        raise Exception(f'Both matrices are not the same dimension! \nMatrix A:{matrix_a} \nMatrix B:{matrix_b}')
    if get_matrix_dimensions(matrix_a) == (2, 2):
        return default_matrix_multiplication(matrix_a, matrix_b)

    A, B, C, D = split_matrix(matrix_a)
    E, F, G, H = split_matrix(matrix_b)

    p1 = strassen(A, matrix_subtraction(F, H))
    p2 = strassen(matrix_addition(A, B), H)
    p3 = strassen(matrix_addition(C, D), E)
    p4 = strassen(D, matrix_subtraction(G, E))
    p5 = strassen(matrix_addition(A, D), matrix_addition(E, H))
    p6 = strassen(matrix_subtraction(B, D), matrix_addition(G, H))
    p7 = strassen(matrix_subtraction(A, C), matrix_addition(E, F))

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

def main():
    A = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
    B = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
    #A = [[1,2],[1,2]]
    #B = [[1,2],[1,2]]
    #print(matrix_multiply(A,B))
    print(matrix_multiply_divide(A,B))
    print(strassen(A,B))
    
main()
