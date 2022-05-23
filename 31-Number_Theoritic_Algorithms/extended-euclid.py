def extended_euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (g, x, y) = extended_euclid(b, a % b)
        return (g, y, x - (a // b) * y)

print(extended_euclid(99, 78))