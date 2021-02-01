import math
def count_inversions(A, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        left = count_inversions(A, p, q)
        right = count_inversions(A, q + 1, r)
        if left == None:
            left = 0
        if right == None:
            right = 0
        inversions = merge_inversions(A, p, q, r) + left + right
        return inversions

def merge_inversions(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L,R = [0]*(n1+1),[0]*(n2+1)
    for i in range(0,n1):
        L[i] = A[p + i]
    for j in range(0,n2):
        R[j] = A[q + j + 1]
    L[n1] = math.inf
    R[n2] = math.inf
    i = 0
    j = 0
    inversions = 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            inversions = inversions + n1 - i
            A[k] = R[j]
            j = j + 1
    return inversions

a = [2,3,8,6,1]
print(count_inversions(a,0,len(a)-1))
