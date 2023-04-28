import random 

def morris_counter(bits):
    """
he approximate counting algorithm allows the counting of a large number of events using a small amount of memory. Invented in 1977 by
 Robert Morris (cryptographer) of Bell Labs, it uses probabilistic techniques to increment the counter
 Wikipedia : When incrementing the counter, "flip a coin" the number of times of the counter's current value. If it comes up "Heads" each time, then increment the counter. Otherwise, do not increment it.

Here we instead always incrementing count, we increment count with probability of 1/2 to the power of count and we return 2 to the power of count minus 1.

    """
    count = 0
    while True:
        if count < 2**bits -1:
            prob = random.random()
            if prob < 1/(2**count):
                count += 1
        else:
            break
    return 2**count -1

bits = 100
print(morris_counter(bits))