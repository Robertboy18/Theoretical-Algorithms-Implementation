from _typeshed import IdentityFunction



def linear_time(A):
    max_value = -10e10
    low, high = 0, 0
    final = 0
    l = 0
    for i in range(len(A)):
        final += A[i]
        if final > max_value:
            max_value = final
            low = l
            high = i
        if final < 0:
            final = 0
            l = i+1
    return (low, high, max_value)

A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(linear_time(A))

