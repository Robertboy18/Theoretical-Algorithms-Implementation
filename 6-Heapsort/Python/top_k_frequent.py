import unittest
from collections import Counter
import heapq

# Author: Robert Joseph

def top_k_counter(x, k):
    """
    This function returns the top k elements (largest) in the input list x
    based on their frequency of occurrence.
    """
    # If k is equal to the length of x, return all elements
    if k == len(x):
        return x
    
    # Count the occurrences of each element in x
    count = Counter(x)
    
    # Obtain the top k elements using a min-max heap
    # Time complexity: O(n log k) if k < n, O(n) if k = n
    # Space complexity: O(k + n)
    return heapq.nlargest(k, count.keys(), key=count.get)


class TestTopKCounter(unittest.TestCase):
    def test_top_k_counter(self):
        # Test with a list containing duplicate elements
        x = [1, 2, 1, 425, 122, 13, 24235]
        k = 3
        self.assertEqual(top_k_counter(x, k), [1, 122, 13])

        # Test with a list containing all unique elements
        x = [4, 2, 6, 1, 9]
        k = 2
        self.assertEqual(top_k_counter(x, k), [1, 2])

        # Test with a list where k equals the length of x
        x = [1, 2, 3, 4, 5]
        k = 5
        self.assertEqual(top_k_counter(x, k), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
