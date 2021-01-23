# return 3^n - 2^n

def three_two(n):
    if n<=1:
        return n
    else:
        return 5*three_two(n-1) - 6*three_two(n-2)

print(three_two(30))
