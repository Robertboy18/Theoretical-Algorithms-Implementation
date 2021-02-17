def peak_finding_2d(arr,f,l,mid):
    element = -1000000000
    index = 0
    for i in range(len(arr)):
        if arr[i][mid] > element:
            element = max(element,arr[i][mid])
            index = i
    print(element,i)
    if mid == 0 or mid == len(arr[0])-1:
        print(element)
        return element
    if arr[i][mid-1] <= element and element >= arr[i][mid+1]:
        return element
    if element <= arr[i][mid+1]:
        peak_finding_2d(arr,f,l,mid + mid//2)
    else:
        peak_finding_2d(arr,f,l,mid - mid//2)
    
        

t = [ [ 10, 8, 10, 10 ], 
        [ 14, 13, 12, 11 ], 
        [ 15, 11, 4, 10 ], 
        [ 16, 17, 19, 20 ] ] 

peak_finding_2d(t,4,4,2)
    
