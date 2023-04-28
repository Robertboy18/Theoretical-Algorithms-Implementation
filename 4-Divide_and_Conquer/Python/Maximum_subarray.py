def max_subarray(A,low,high):
    if high == low:
        return (low,high,A[low])
    else:
        mid = (low+high)//2
        (left_low,left_high,left_sum) = max_subarray(A,low,mid)
        (right_low,right_high,right_sum) = max_subarray(A,mid+1,high)
        (cross_low,cross_high,cross_sum) = max_crossing_subarray(A,low,mid,high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_sum,left_low,left_high)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_sum,right_low,right_high)
        else:
            return (cross_sum,cross_low,cross_high)

def max_crossing_subarray(A,low,mid,high):
    left_sum = -float('inf')
    sum = 0
    max_left = 0
    for i in range(mid,low-1,-1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -float('inf')
    sum = 0
    max_right = 0
    for i in range(mid+1,high+1):
        sum += A[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    return (max_left,max_right,left_sum+right_sum)

A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(max_subarray(A,0,len(A)-1))

# exercise : 4.1-4
c = [i > 0 for i in A]
if len(c)> 0:
    print(max_subarray(A,0,len(A)-1))
else:
    print(0)