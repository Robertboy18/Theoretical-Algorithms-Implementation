import heapq

def top_k(x,k):
    # obtain the k-th element in x (largest)
    # time complexity : 0(klogn + n)
    # space complexity : 0(n)
    x = [-i for i in x]
    heapq.heapify(x)
    for i in range(k-1):
        heapq.heappop(x)
    print(-1*x[0])

def top_k_optimized(x,k):
    # obtain the top k-th element in x (largest)
    # time complexity : 0(nlogk)
    # space complexity : 0(k)
    heap = []
    for i in range(len(x)):
        if len(heap) <= k - 1:
            heapq.heappush(heap,x[i])
        else:
            if x[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,x[i])
            else:
                continue
    print(heap[0])
    

x = [1,2,1,425,122,13,24235]
(top_k(x,3))
(top_k_optimized(x,3))