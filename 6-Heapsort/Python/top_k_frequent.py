from collections import Counter
import heapq

def top_k_counter(x,k):
    # obtain the top k elements in x (largest)
    # time complexity : 0(nlogk) if k < n and 0(n) if k = n
    # space complexity : 0(k + n)
    if k == len(x):
        return x
    count = Counter(x)  
    return heapq.nlargest(k, count.keys(), key=count.get)

print(top_k_counter([1,2,1,425,122,13,24235],3))

