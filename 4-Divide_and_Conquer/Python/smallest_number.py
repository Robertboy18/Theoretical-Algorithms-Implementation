import unittest

# Author: Robert Joseph

def smallest_number(arr, f, l):
    """
    This function recursively finds the smallest number in the subarray
    arr[f:l+1], using the divide and conquer strategy of binary search.
    """
    # Base case: subarray has only one element, return it
    if f == l:
        return arr[f]
    else:
        # Divide the subarray into two halves
        mid = (f + l) // 2
        
        # Conquer the subproblems by finding the smallest number in each half
        left_min = smallest_number(arr, f, mid)
        right_min = smallest_number(arr, mid+1, l)
        
        # Combine the solutions by taking the minimum of the two smallest numbers
        return min(left_min, right_min)


class TestSmallestNumber(unittest.TestCase):
    def test_smallest_number(self):
        # Test with sorted array
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(smallest_number(arr, 0, len(arr)-1), 1)

        # Test with unsorted array
        arr = [5, 3, 2, 4, 1]
        self.assertEqual(smallest_number(arr, 0, len(arr)-1), 1)

        # Test with array of size 1
        arr = [1]
        self.assertEqual(smallest_number(arr, 0, len(arr)-1), 1)


if __name__ == '__main__':
    unittest.main()
