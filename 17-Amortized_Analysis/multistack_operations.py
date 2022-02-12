def multipop(S,k):
    # amortized analysis : average case is 0(n)
    while S:
        yield S.pop()

def multipush(S,k):
    # amortized analysis : average case is 0(1)
    S.append(k)

S = [1,2,3,4,5]
for i in multipop(S,2):
    print(i)