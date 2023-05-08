import unittest

# Author: Robert Joseph

def max_subarray(A, low, high):
    """
    This function finds the maximum subarray of the given array A
    between the indices low and high using a divide-and-conquer approach.
    """
    if high == low:
        # base case: array has only one element
        return (low, high, A[low])
    else:
        # divide the array into two halves
        mid = (low + high) // 2
        
        # find the maximum subarrays of the left and right halves recursively
        (left_low, left_high, left_sum) = max_subarray(A, low, mid)
        (right_low, right_high, right_sum) = max_subarray(A, mid+1, high)
        
        # find the maximum subarray that crosses the midpoint
        (cross_low, cross_high, cross_sum) = max_crossing_subarray(A, low, mid, high)
        
        # return the maximum of the three subarrays
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


def max_crossing_subarray(A, low, mid, high):
    """
    This function finds the maximum subarray that crosses the midpoint
    in the given array A between the indices low and high.
    """
    left_sum = -float('inf')
    sum = 0
    max_left = 0
    
    # find the maximum subarray that ends at the midpoint
    for i in range(mid, low-1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
            
    right_sum = -float('inf')
    sum = 0
    max_right = 0
    
    # find the maximum subarray that starts at the midpoint
    for i in range(mid+1, high+1):
        sum += A[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
            
    # return the maximum subarray that crosses the midpoint
    return (max_left, max_right, left_sum+right_sum)


class TestMaxSubarray(unittest.TestCase):
    def test_max_subarray(self):
        # test with array A = [1, -3, 2, 1, -1]
        A = [1, -3, 2, 1, -1]
        n = len(A)
        self.assertEqual(max_subarray(A, 0, n-1), (2, 3, 3))

        # test with array A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        n = len(A)
        self.assertEqual(max_subarray(A, 0, n-1), (3, 6, 6))

        # test with array A = [-1, -2, -3, -4, -5]
        A = [-1, -2, -3, -4, -5]
        n = len(A)
        self.assertEqual(max_subarray(A, 0, n-1), (0, 0, -1))


if __name__ == '__main__':
    unittest.main()
