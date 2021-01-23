def selection(z):
    for i in range(0,len(z)-1):
        k = i
        for j in range(i+1,len(z)):
            if z[j] < z[k]:
                k = j
        z[i],z[k] = z[k],z[i]
    return z

a = [1,24,5,6,7,8,-232,35,5,67]

print(selection(a))
