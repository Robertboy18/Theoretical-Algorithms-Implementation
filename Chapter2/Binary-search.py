def binary_search(z,x,low,high):
    while low <= high:
        mid = (low+high)//2
        if z[mid] == x:
            return True
        elif z[mid] > x:
            low = mid+1
        else:
            high = mid-1
    return False

a = [1,24,5,6,7,8,-232,35,5,67]
k = sorted(a)
print(k) # [-232, 1, 5, 5, 6, 7, 8, 24, 35, 67]
print(binary_search(k,23,0,len(k)))
