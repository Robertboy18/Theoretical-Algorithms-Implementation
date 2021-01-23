def max_linear_search_index(n,m):
    c = -1
    for i in range(len(n)):
        if n[i] == m:
            c = max(c,i)
    if c == -1:
        return "NIL"
    else:
        return c
    
a = [1,2,34,23,44,44,44,44,4453]
print(max_linear_search_index(a,44))
