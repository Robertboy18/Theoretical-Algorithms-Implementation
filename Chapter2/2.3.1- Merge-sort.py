import math
def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q

    L,R = [0]*(n1+1), [0]*(n2+1)
    for i in range(0,n1):
        L[i] = A[p+i]
    for j in range(0,n2):
        R[j] = A[q+j+1]
    L[n1] = math.inf
    R[n2] = math.inf
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A,p,r):
    if p < r:
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

a = [1,24,5,6,7,8,-232,35,5,67]

merge_sort(a,0,len(a)-1)
print(a)

