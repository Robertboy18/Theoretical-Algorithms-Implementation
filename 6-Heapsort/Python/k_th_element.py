import heapq
import unittest

# Author: Robert Joseph

def top_k(x, k):
    """
    This function finds the k-th largest element in the list x using a min-heap.
    Time complexity: O(klogn + n)
    Space complexity: O(n)
    """
    # Convert elements to negative to simulate a max-heap behavior
    x = [-i for i in x]
    heapq.heapify(x)

    # Remove k-1 elements from the heap
    for _ in range(k-1):
        heapq.heappop(x)

    # Print the k-th largest element
    return -1 * x[0]


def top_k_optimized(x, k):
    """
    This function finds the k-th largest element in the list x using an optimized approach.
    Time complexity: O(nlogk)
    Space complexity: O(k)
    """
    heap = []

    for i in range(len(x)):
        if len(heap) <= k - 1:
            heapq.heappush(heap, x[i])
        else:
            if x[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, x[i])
            else:
                continue

    # Print the k-th largest element
    return heap[0]


class TestTopK(unittest.TestCase):
    def test_top_k(self):
        # Test with list x = [1, 2, 1, 425, 122, 13, 24235]
        x = [1, 2, 1, 425, 122, 13, 24235]
        self.assertEqual(top_k(x, 3), 122)

        # Test with list x = [10, 20, 30, 40, 50]
        x = [10, 20, 30, 40, 50]
        self.assertEqual(top_k(x, 2), 40)

        # Test with list x = [5, 2, 8, 9, 1]
        x = [5, 2, 8, 9, 1]
        self.assertEqual(top_k(x, 4), 2)


if __name__ == '__main__':
    unittest.main()
