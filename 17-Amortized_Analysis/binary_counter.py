def binary_counter(A):
    """
    A function that counts the number of 1s in a binary number.
    """
    count = 0
    while A > 0:
        if A % 2 == 1:
            count += 1
        A = A // 2
    return count

def increment(A):
    # cost of each increment operatrion is linear in the number of
    # bits flipped
    # amortized analysis : average case is 0(1)
    i = 0
    while i < len(A) and A[i] == 1:
        A[i] = 0
        i += 1
    if i < len(A):
        A[i] = 1