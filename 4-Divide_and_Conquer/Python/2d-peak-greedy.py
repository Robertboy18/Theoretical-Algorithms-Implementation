import unittest

# Author: Robert Joseph

def max_peak(arr):
    """
    This function finds the maximum peak in a 2D array, where a peak
    is defined as an element that is greater than its four neighbors:
    above, below, to the left, and to the right.
    
    The time complexity of this function is O(n*m), where n is the number of rows in the array and m is the number of columns. This is because the function iterates over each element in the interior of the array once and performs a constant number of operations for each element.
    """
    # iterate over all elements in the interior of the array
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            # check if the element is a peak
            if arr[i][j] > arr[i+1][j] and arr[i][j] > arr[i-1][j] and \
            arr[i][j] > arr[i][j+1] and arr[i][j] > arr[i][j-1]:
                return arr[i][j]
    
    # if no peak is found, return False
    return False


class TestMaxPeak(unittest.TestCase):
    def test_max_peak(self):
        # Test with a peak in the center
        arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_peak(arr), 5)

        # Test with a peak in the top left corner
        arr = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        self.assertEqual(max_peak(arr), 9)

        # Test with no peak
        arr = [[1, 2, 3], [4, 5, 6], [3, 2, 1]]
        self.assertFalse(max_peak(arr))


if __name__ == '__main__':
    unittest.main()
