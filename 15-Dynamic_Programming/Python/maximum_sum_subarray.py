import unittest

# Author: Robert Joseph

def maximum_subarray(arr):
    """
    This function finds the maximum sum of a subarray in the given array using the brute force approach.
    It iterates over all possible subarrays and keeps track of the maximum sum encountered.
    """
    # Initialize the maximum sum with negative infinity
    m = float('-inf')
    
    # Iterate over each element as a potential starting point of a subarray
    for i in range(len(arr)):
        # Calculate the sum of subarrays starting at index i
        subarray_sum = 0
        for j in range(i, len(arr)):
            subarray_sum += arr[j]
            
            # Update the maximum sum if the current subarray sum is greater
            m = max(m, subarray_sum)
    
    # Return the maximum sum
    return m


class TestMaximumSubarray(unittest.TestCase):
    def test_maximum_subarray(self):
        # Test with positive numbers
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(maximum_subarray(arr), 15)

        # Test with negative numbers
        arr = [-1, -2, -3, -4, -5]
        self.assertEqual(maximum_subarray(arr), -1)

        # Test with mixed positive and negative numbers
        arr = [1, -2, 3, -4, 5]
        self.assertEqual(maximum_subarray(arr), 5)


if __name__ == '__main__':
    unittest.main()
