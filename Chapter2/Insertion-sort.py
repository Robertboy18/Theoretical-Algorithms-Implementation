def insertion(d):
    for i in range(1,len(d)):
        key = d[i]
        j = i-1
        while j >= 0 and key<d[j]: 
            d[j+1] = d[j]
            j -= 1
        d[j+1] = key
    return d

print(insertion([334,23,2,4]))
