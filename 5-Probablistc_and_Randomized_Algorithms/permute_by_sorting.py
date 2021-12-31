import random
import math

def permute_by_sorting(A):
    # running time : O(nlogn) 
    # can be brought down to 0(n) 
    n = len(A)
    P = [0] * n
    for i in range(n):
        P[i] = random.randint(0,n**3)
    A = [A[i] for i in sorted(range(n), key=lambda i: P[i])]
    return A

A = [1,2,3,4,5,6,7,8,9,10]
print(permute_by_sorting(A))