import sys
def cutRod(arr,n):
    # Time : O(2^n)
    # Number of subsets = 2^(n-1)
    if n == 0:
        return 0
    q = -sys.maxsize
    for i in range(n):
        q = max(q,arr[i] + cutRod(arr,n-i-1))
    return q
    
def memoized_cut(arr,n):
    # Top to down approach 
    # 0(n^2)
    r = [i for i in range(n)]
    for i in range(n):
        r[i] = -sys.maxsize
    return cutRod_memoized(arr,n,r)

def cutRod_memoized(arr,n,r):
    if r[n-1]>= 0:
        return r[n-1]
    if n == 0:
        q = 0
    else:
        q = -sys.maxsize
        for i in range(1,n):
            q =max(q,arr[i] + cutRod_memoized(arr,n-i-1,r))
    r[n-1] = q
    return q 

def bottom_up_cut_rod(arr, n):
    # Time : 0(n^2)
    # use formulae : r_n = max_{1<=i<=n} (p[i] + r[n-i],p[n]) 
    r = [0 for x in range(n+1)]
    r[0] = 0
    for i in range(1, n+1):
        q = -sys.maxsize
        for j in range(i):
            q = max(q, arr[j] + r[i-j-1])
        r[i] = q
    return r[n]
        
            
arr = [1, 5, 8]
size = len(arr)
print("Maximum value is", bottom_up_cut_rod(arr, size))
