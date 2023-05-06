import math

# Author: Robert Joseph 

def insertion_sort_time(n):
    return 8 * n**2

def merge_sort_time(n):
    return 64 * n * math.log2(n)

def f(n):
    return n / 8 - 8 * math.log2(n)

def find_smallest_n():
    a = 1
    b = 1000
    tol = 1e-6
    
    while b - a > tol:
        c = (a + b) / 2
        if f(c) < 0:
            a = c
        else:
            b = c
    
    return math.ceil(b)

n = find_smallest_n()
print(f"Insertion sort beats merge sort for n <= {n}")
