def plusOne(A):
    c = 0
    t = -1
    choice = True
    while choice:
        c = A[t]%10
        if c == 9 and len(A) == -t:
            A.insert(0,1)
            choice = False
        if c!=9:
            A[t] += 1
            choice = False
        else:
            A[t] = 0
            t = t - 1
    for i in range(len(A)):
        if A[i]!=0:
            return A[i:]
    return A
#z = [1,10,0]          
z = [0,0,0,0,9,0,0,0,1,9,9,9]
print(plusOne(z))
