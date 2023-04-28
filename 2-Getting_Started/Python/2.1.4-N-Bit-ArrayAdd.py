def bit_add(x,y):
    z = [0]*(len(x)+1)
    c = 0
    for i in range(len(x)):
        c = x[i] +y[i] + z[i] 
        z[i] = c%2
        z[i+1] = c//2
    return z

a = [1,1,0]
b = [0,1,1]
print(bit_add(a,b))
