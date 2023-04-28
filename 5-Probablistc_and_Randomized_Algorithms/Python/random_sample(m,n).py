import random 

def random_sample_standard(m,n):
    # expected running time : O(m*n)
    A = [i for i in range(n)]
    random.shuffle(A)
    print("Sample is :", A[:m])
    return A[:m]

S = []
def random_sample(m,n):
    if m == 0:
        return []
    else:
        S = random_sample(m-1,n-1)
        i = random.randint(0,n-1)
        if i in S:
            S.append(n)
        else:
            S.append(i)
        return S
    
print(random_sample(5,10))