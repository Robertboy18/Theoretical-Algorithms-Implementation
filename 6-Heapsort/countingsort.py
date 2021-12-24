def counting_sort(arr):
    """
    0(N+K) Complexity - 0(N)
    """
    array = dict()
    for i in range(len(arr)):
        array[i] = 0
    for j in range(len(arr)):
        array[arr[j]] += 1
    final = ""
    for key,value in array.items():
        final += str(key)*value
    final = [int(i) for i in final]
    return list(final)
        
    
arr = [3,4,3,2,4]
print(counting_sort(arr))
