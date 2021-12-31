import random

def random_search(A,element):
    # max searches = n
    # expected running time : O(n)
    checked = [False]*len(A)
    j = 0
    while j < len(A):
        i = random.randint(0,len(A)-1)
        if not checked[i]:
            checked[i] = True
            j += 1
        if A[i] == element:
            return i
    return -1

A = [1,2,3,4,5,6,7,8,9,10]
print(random_search(A,5))
print(random_search(A,11))