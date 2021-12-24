
def semi_sorted(arr, f, l):
    if f == l:
        return arr[f]
    mid = (f + l)//2
    if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
        return arr[mid]
    if arr[mid] > arr[mid + 1]:
        return semi_sorted(arr, f, mid)
    else:
        return semi_sorted(arr, mid + 1, l)
a = [1,1,400,221,100,4,3]
print(semi_sorted(a,0,len(a)))
