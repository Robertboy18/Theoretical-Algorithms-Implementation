def merge_sort(A):
    if len(A) > 1:
        mid = (len(A))//2
        L = A[:mid]
        R = A[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1


a = [1,24,5,6,7,8,-232,35,5,67]

(merge_sort(a))
print(a)
