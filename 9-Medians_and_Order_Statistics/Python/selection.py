import heapq

def find_ith_largest(A, i):
    # Build a max heap from A
    heap = [-x for x in A]
    heapq.heapify(heap)

    # Extract the i-1 largest elements from the heap
    for j in range(i-1):
        heapq.heappop(heap)

    # The i-th largest element is now at the root of the heap
    return -heapq.heappop(heap)

A = [3, 2, 1, 5, 4, 6, 7, 8, 9, 10]
i = 3
print(find_ith_largest(A, i))
