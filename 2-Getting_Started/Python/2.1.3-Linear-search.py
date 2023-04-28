def linear_search(x,m):
    for i in range(len(x)):
        if x[i] == m:
            return i
    return "NIL"

print(linear_search([9888,22233,22,4,423423,2],10))
