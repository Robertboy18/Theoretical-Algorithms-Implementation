import collections
def dutch_flag(L):
    # Time - 0(N)
    # Space - 0(N)
    l = dict(collections.Counter(L))
    k = []
    r = l['R']
    w = l['W']
    b = l['B']
    for __ in range(r):
        k.append("R")
    for __ in range(w):
        k.append("W")
    for __ in range(b):
        k.append("B")
    return k
    
def dutch_flag1(L):
    # Time - 0(N)
    # Space - 0(1)
    r = L.count("R")
    w = L.count("W")
    b = L.count("B")
    for i in range(r):
        L[i] = "R"
    for j in range(r,r+w):
        L[j] = "W"
    for k in range(r+w,r+w+b):
        L[k] = "B"
    return L
        

l = ['R','B','W','R','B','R','R']
print(l)
print(dutch_flag(l))
print(dutch_flag1(l))
