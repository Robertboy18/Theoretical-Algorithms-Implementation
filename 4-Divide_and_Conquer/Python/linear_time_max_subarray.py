import unittest

# Author: Robert Joseph

def linear_time(A):
    """
    This function implements the Kadane's algorithm for finding the maximum
    subarray sum of an array A in linear time.
    """
    # initialize variables
    max_value = A[0]
    low, high = 0, 0
    final = A[0]
    l = 0
    
    # iterate over each element of the array
    for i in range(1, len(A)):
        # add the current element to the running sum
        if final + A[i] > A[i]:
            final += A[i]
        else:
            final = A[i]
            l = i
        
        # if the running sum is greater than the current max value,
        # update the max value and the endpoints of the subarray
        if final > max_value:
            max_value = final
            low = l
            high = i
    
    # return the endpoints of the maximum subarray and its sum
    return (low, high, max_value)


class TestLinearTime(unittest.TestCase):
    def test_linear_time(self):
        # Test with array A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected_output = (3, 6, 6)
        self.assertEqual(linear_time(A), expected_output)

        # Test with array A = [1, -2, 3, -4, 5, -6, 7, -8, 9]
        A = [1, -2, 3, -4, 5, -6, 7, -8, 9]
        expected_output = (0, 8, 16)
        self.assertEqual(linear_time(A), expected_output)

        # Test with array A = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
        A = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
        expected_output = (0, 0, -1)
        self.assertEqual(linear_time(A), expected_output)


if __name__ == '__main__':
    unittest.main()
