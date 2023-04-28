import random

def randomize_in_place(A):
    # Expected 0(N) time
    n = len(A)
    for i in range(n):
        j = random.randint(i, n-1)
        A[i], A[j] = A[j], A[i]
    return A

A = [1,2,3,4,5,6,7,8,9,10]
print(randomize_in_place(A))