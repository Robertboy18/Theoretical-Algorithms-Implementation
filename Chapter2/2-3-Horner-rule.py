def horner_rule(a,n,x):
    y = a[0]
    for i in range(1,n):
        y = a[i] + x*y
    return y
a = [1,2,2,54,699]
# [1,2,3,4,5,6] x = 5
print(horner_rule(a,5,3))
