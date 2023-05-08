import unittest

# Author: Robert Joseph

def max_sub_prob(arr):
    """
    This function implements the Kadane's algorithm to find the maximum sum of a
    contiguous subarray of an array arr.
    """
    max_sum = 0  # initialize the maximum sum to 0
    cur_sum = 0  # initialize the current sum to 0
    
    for i in range(len(arr)):
        cur_sum += arr[i]  # add the current element to the current sum
        
        if cur_sum > max_sum:
            max_sum = cur_sum  # update the maximum sum if the current sum is larger
         
        if cur_sum < 0:
            cur_sum = 0  # reset the current sum if it becomes negative
    
    return max_sum


class TestMaxSubProb(unittest.TestCase):
    def test_max_sub_prob(self):
        # Test with array [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_sub_prob(arr), 6)

        # Test with array [1, -2, 3, -4, 5, -6, 7, -8, 9]
        arr = [1, -2, 3, -4, 5, -6, 7, -8, 9]
        self.assertEqual(max_sub_prob(arr), 9)

        # Test with array [-2, -3, 4, -1, -2, 1, 5, -3]
        arr = [-2, -3, 4, -1, -2, 1, 5, -3]
        self.assertEqual(max_sub_prob(arr), 7)


if __name__ == '__main__':
    unittest.main()
