def sieve(n):
    k = []
    for i in range(2,n+1):
        if i not in k:
            print(i)
            for j in range(i*i,n+1,i):
                k.append(j)

sieve(10)
