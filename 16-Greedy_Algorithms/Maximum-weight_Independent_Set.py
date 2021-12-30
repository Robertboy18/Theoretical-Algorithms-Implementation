#Let X be a finite set of elements with two partitions A, B (figure 1(a)). Each element x ∈ X has weight w(x).
#Also, we are given three values bA, bB, bX ∈ Z≥0. We wish to find the maximum weight subset Y ⊆ X such that
#1. |Y | ≤ bX,
#2. |Y ∩ A| ≤ bA, and
#3. |Y ∩ B| ≤ bB,
#where weight of Y is equal to sum i∈Y w(x).


def maximum(X,weights,A,B,bA,bB,bX):
    Y = []
    X = [x for _, x in sorted(zip(weights, X))]
    for i in range(len(X)):
            # satisfying the properties
            Y.append(X[i])
            value1 = len(Y)
            value2 = len(list(set(Y) & set(A)))
            value3 = len(list(set(Y) & set(B)))
            if value1 <= bX and value2 <= bA and value3 <= bB:
                pass
            else:
                Y.remove(X[i])
    return Y

X = {1,2,3,4,5,6,7,8,9,10}
A = {1,2,3,4,5}
B = {6,7,8,9,10}
bA = 12
bB = 31
bX = 33
weights = {2,3,3,4,5,6,7,8,9,10}
print(maximum(X,weights,A,B,bA,bB,bX))