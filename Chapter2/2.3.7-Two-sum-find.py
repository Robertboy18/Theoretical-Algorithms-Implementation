def binary_search(arr,x):
    l,f = 0,len(arr)
    while l <= f:
        q = (l+f)//2
        if arr[q] == x:
            return True
        elif arr[q] > x:
            f = q-1
        else:
            l = q+1
    return False
def sum_find(arr,x):
    sorted(arr)
    for i in range(len(arr)):
        if binary_search(arr,x - arr[i]):
            return True
    return False
a = [1,2,699,54]
print(sum_find(a,57))
