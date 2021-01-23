def maximum(z):
    c = -99999999999999
    for i in z:
        c = max(c,i)
    return c
a = [1,24,5,6,7,8,-232,35,5,67]

print(maximum(a))
