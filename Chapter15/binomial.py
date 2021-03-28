import sys
n = 5
k = 3
def binomial_recurrsive(n,k):
    # Time
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
print("Binomial",binomial(n,k))
print(soln)
