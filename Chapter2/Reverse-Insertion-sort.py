def insertion(d):
    for i in range(1,len(d)):
        key = d[i]
        j = i-1
        while j >= 0 and key>d[j]: 
            d[j+1] = d[j]
            j -= 1
        d[j+1] = key
    return d

print(insertion([9888,22233,22,4,423423,2]))
