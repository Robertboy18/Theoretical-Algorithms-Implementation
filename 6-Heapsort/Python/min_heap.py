import heapq

# Create an array
minHeap = []

# Heapify the array into a Min Heap
heapq.heapify(minHeap)

# Add 4, 3，1，2 respectively to the Min Heap
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 1)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Check all elements in the Min Heap
print("minHeap: ", minHeap)

# Get the top element of the Min Heap
max_number = minHeap[0]
print("top of the heap number: ", max_number)

# Delete the top element in the Min Heap
popNum = heapq.heappop(minHeap)
print("pop number: ", popNum)

# Check the top element after deleting 1, the result is 2
print("top of the heap number: ", minHeap[0])

# Check the number of elements in the Min Heap
# Which is also the length of the Min Heap
size = len(minHeap)
print("minHeap size: ", size)

