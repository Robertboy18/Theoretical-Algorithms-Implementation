def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                arr[j],arr[i] = arr[i],arr[j]
    return arr
a = [1,2,2,54,699]
# [1,2,3,4,5,6] x = 5
print(bubble_sort(a))
