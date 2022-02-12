import heapq

def top_k(x,k):
    # obtain the top k elements in x (smallest)
    # time complexity : 0(klogn + n)
    # space complexity : 0(n)
    heapq.heapify(x)
    for i in range(k):
        print(heapq.heappop(x)) 

def top_k_optimized(x,k):
    pass
    

x = [1,2,1,425,122,13,24235]
print(top_k(x,3))