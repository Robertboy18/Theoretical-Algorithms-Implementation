import random 

def randomized_hire_assistant(n):
    # expected hiring cost : O(times*logn)
    A = [i for i in range(n)]
    random.shuffle(A)
    print("Candidates are( rankings) :", A)
    best = 0
    times = 0
    for i in range(1,n):
        if A[i] > A[best]:
            times += 1
            best = i
    return times

n = 10
print(randomized_hire_assistant(n))