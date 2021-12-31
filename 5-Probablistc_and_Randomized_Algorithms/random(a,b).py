import random
import math

def pow2(p):
    r = 0
    for i in range(p):
        r = 2 * r + random.randint(0, 1)
    return r

def random1(a, b):
    # running time : 0(log(b-a))
    """https://stackoverflow.com/questions/8692818/how-to-implement-randoma-b-with-only-random0-1"""
    p = math.ceil(math.log2(b - a + 1))
    while True:
        r = pow2(p)
        if r > a + b:
            continue
        else:
            return a + r

print(random1(1,10))