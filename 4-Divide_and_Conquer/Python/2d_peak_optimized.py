import unittest

# Author: Robert Joseph

def peak_finding_2d(arr, f, l, mid):
    """
    This function finds a peak element in a 2D array arr.
    A peak element is an element that is greater than or equal to its four neighbors,
    which are the elements that are directly above, below, to the left, and to the right of it.
    The function assumes that the input array is not empty and has at least one peak element.
    
    The time complexity of this function is O(m log n), where m is the number of rows and n is the number of columns in the input array. This is because the function recursively halves the search space along the middle column until it finds a peak element, and each recursion takes O(m) time to scan a column of the array.
    """
    # initialize the maximum element in the middle column and its index
    element = -1000000000
    index = 0
    for i in range(len(arr)):
        # find the maximum element in the middle column
        if arr[i][mid] > element:
            element = max(element, arr[i][mid])
            index = i
    # print the maximum element and its row index (for debugging purposes)
    print(element, index)
    # check if the maximum element is a peak element
    if mid == 0 or mid == len(arr[0])-1 or (arr[index][mid-1] <= element and element >= arr[index][mid+1]):
        return element
    # if not, recurse on the half of the array with the higher neighbor
    elif element <= arr[index][mid+1]:
        return peak_finding_2d(arr, f, l, mid + mid//2)
    else:
        return peak_finding_2d(arr, f, l, mid - mid//2)


class TestPeakFinding2D(unittest.TestCase):
    def test_peak_finding_2d(self):
        # Test with a 3x3 array with a peak at the center
        arr = [ [ 1, 2, 3 ], 
                [ 4, 5, 6 ], 
                [ 7, 8, 9 ] ]
        self.assertEqual(peak_finding_2d(arr, 0, 2, 1), 5)

        # Test with a 3x3 array with a peak at the corner
        arr = [ [ 10, 8, 6 ], 
                [ 9, 7, 5 ], 
                [ 8, 6, 4 ] ]
        self.assertEqual(peak_finding_2d(arr, 0, 2, 1), 10)

        # Test with a 4x4 array with a peak at the edge
        arr = [ [ 10, 8, 10, 10 ], 
                [ 14, 13, 12, 11 ], 
                [ 15, 11, 4, 10 ], 
                [ 16, 17, 19, 20 ] ]
        self.assertEqual(peak_finding_2d(arr, 0, 3, 1), 17)


if __name__ == '__main__':
    unittest.main()
