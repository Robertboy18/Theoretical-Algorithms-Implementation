def maximum_differnce(z):
    c = -99999999999999
    for i in range(1,len(z)):
        c = max(c,abs(z[i]-z[i-1]))
    return c
a = [1,24,5,6,7,8,-232,35,5,67]

print(maximum_differnce(a))
