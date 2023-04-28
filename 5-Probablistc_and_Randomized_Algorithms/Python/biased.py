import numpy as np

p = 0.2
def biased_random():
    return np.random.binomial(1, p)

def biased():
    # Expected = (1-2p(p-1))/(2p(p-1))
    while True:
        x = biased_random() # (p(1-p))
        y = biased_random() # (p(1-p))
        if x > y:
            return 1
        else:
            return 0