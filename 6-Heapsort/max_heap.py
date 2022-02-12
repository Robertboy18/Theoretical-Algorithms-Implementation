import heapq

# Create an array
maxheap = []

# Heapify the array into a Min Heap
heapq.heapify(maxheap)

# Add --3，-1，-2, -4 respectively to the Min Heap
# no standard implementation for max heap in heapq
# have to multiply by -1 to make it a max heap
heapq.heappush(maxheap, -3)
heapq.heappush(maxheap,-1)
heapq.heappush(maxheap, -2)
heapq.heappush(maxheap, -4)

# Check all elements in the Min Heap
print("maxHeap: ", maxheap)

# Get the top element of the Min Heap
max_number = maxheap[0]
print("top of the heap number: ", -1*max_number)

# Delete the top element in the Min Heap
popNum = heapq.heappop(maxheap)
print("pop number: ", popNum)

# Check the top element after deleting 1, the result is 2
print("top of the heap number: ", -1*maxheap[0])

# Check the number of elements in the Min Heap
# Which is also the length of the Min Heap
size = len(maxheap)
print("maxheap size: ", size)

