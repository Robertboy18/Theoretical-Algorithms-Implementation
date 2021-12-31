def monge(A):
    m = len(A)
    n = len(A[0])
    for i in range(m-1):
        for j in range(n-1):
            if A[i][j] + A[i+1][j+1] > A[i][j+1] + A[i+1][j]:
                return False
    return True
