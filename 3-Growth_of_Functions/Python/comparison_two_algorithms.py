import time
import sys
import numpy as np
import matplotlib.pyplot as plt

# Author: Robert Joseph

def compare_algorithms(algo1, algo2, input_sizes):
    time1 = []
    time2 = []
    space1 = []
    space2 = []
    
    for n in input_sizes:
        list_values = np.random.randint(0, 100, n)
        # measure time complexity
        start_time = time.time()
        algo1(list_values)
        time1.append(time.time() - start_time)
        
        start_time = time.time()
        algo2(list_values)
        time2.append(time.time() - start_time)
        
        # measure space complexity
        size1 = sys.getsizeof(algo1(list_values))
        size2 = sys.getsizeof(algo2(list_values))
        space1.append(size1)
        space2.append(size2)
        
    # find when algo1 beats algo2 in terms of time complexity
    time_ratio = [t2 / t1 for t1, t2 in zip(time1, time2)]
    index = max(range(len(input_sizes)), key=lambda i: time_ratio[i])
    n = input_sizes[index]
    ratio = time_ratio[index]
    print(f"{algo1.__name__} beats {algo2.__name__} in terms of time complexity for n >= {n} (ratio = {ratio:.2f})")
    
    # find when algo1 beats algo2 in terms of space complexity
    space_ratio = [s2 / s1 for s1, s2 in zip(space1, space2)]
    index = max(range(len(input_sizes)), key=lambda i: space_ratio[i])
    n = input_sizes[index]
    ratio = space_ratio[index]
    print(f"{algo1.__name__} beats {algo2.__name__} in terms of space complexity for n >= {n} (ratio = {ratio:.2f})")
    
    # plot time complexity
    plt.plot(input_sizes, time1, label=algo1.__name__)
    plt.plot(input_sizes, time2, label=algo2.__name__)
    plt.xlabel("Input Size")
    plt.ylabel("Time Complexity")
    plt.title("Time Complexity Comparison")
    plt.legend()
    plt.show()
    
    # plot space complexity
    plt.plot(input_sizes, space1, label=algo1.__name__)
    plt.plot(input_sizes, space2, label=algo2.__name__)
    plt.xlabel("Input Size")
    plt.ylabel("Space Complexity")
    plt.title("Space Complexity Comparison")
    plt.legend()
    plt.show()

# example usage
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A

def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
    return A

input_sizes = [10, 100, 1000, 10000]
compare_algorithms(insertion_sort, merge_sort, input_sizes)
