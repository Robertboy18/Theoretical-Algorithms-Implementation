import sys
n = 5
k = 3
def binomial_recurrsive(n,k):
    # Time 0(2^n)
    if n == 0:
        return 0
    else:
        if k == 0 or k == n:
            return 1
        else:
            return binomial_recurrsive(n-1,k-1) + binomial_recurrsive(n-1,k)
        
soln = [[-1 for i in range(k)] for i in range(n)]
def binomial(n,k):
    # Time : 0(n*k)
    # Space : 0(n*k)
    if (soln[n-1][k-1] > -1):
        return soln[n-1][k-1]
    if k == 0 or k == n:
        return 1
    else:
        soln[n-1][k-1] = binomial(n-1,k-1) + binomial(n-1,k)
        return soln[n-1][k-1]
    
def binomial(n,r):
    # Time : 0(n*r)
    # Space : 0(r)
    if n < r:
        return 0
    if (n-r) < r:
        r = n-3
    dp = [0 for __ in range(r+1)]
    dp[0] = 1
    for i in range(1,n+1):
        for j in range(min(i,r),0,-1):
            dp[j] = dp[j] + dp[j-1]
        print(dp)
    return dp[r]
print("Binomial",binomial(n,k))
print(soln)
