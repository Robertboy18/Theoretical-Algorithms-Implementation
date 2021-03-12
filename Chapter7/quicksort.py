def partition(A,low,high):
    pivot = A[high]
    i = low-1
    j = low
    while j < high:
        if A[j] <= pivot:
            i +=1
            A[j],A[i] = A[i],A[j]
        j += 1
    A[i+1],A[high] = A[high],A[i+1]
    return (i+1)

def quicksort(A,low,high):
    if low < high:
        part = partition(A,low,high)
        quicksort(A,low,part-1)
        quicksort(A,low+1,high)


A = [10, 80, 30, 90, 40, 50, 70]
print(quicksort(A,0,len(A)-1))
for i in A:
    print(i)
