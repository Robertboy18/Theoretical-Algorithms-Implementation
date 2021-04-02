
def maximum_subarray(arr):
    m = -INF
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            m = max(m,sum)
        return m
