import unittest

# Author: Robert Joseph

def peak_finding_2d(arr):
    """
    This function finds a peak element in a 2D array arr.
    A peak element is an element that is greater than or equal to its four neighbors,
    which are the elements that are directly above, below, to the left, and to the right of it.
    The function assumes that the input array is not empty and has at least one peak element.
    
    The time complexity of this function is O(m log n), where m is the number of rows and n is the number of columns in the input array. This is because the function recursively halves the search space along the longer dimension until it finds a peak element, and each recursion takes O(n) or O(m) time to scan a row or column of the array.
    """
    m = len(arr)
    n = len(arr[0])
    mid = n // 2
    element = -1000000000
    index = 0

    # Find the maximum element in the middle column
    for i in range(m):
        if arr[i][mid] > element:
            element = arr[i][mid]
            index = i

    # Check if the maximum element is a peak element
    if (mid == 0 or arr[index][mid-1] <= element) and (mid == n-1 or arr[index][mid+1] <= element):
        return element
    elif mid > 0 and arr[index][mid-1] > element:
        # Recurse on the half of the array with the higher neighbor
        return peak_finding_2d([row[:mid] for row in arr])
    else:
        return peak_finding_2d([row[mid+1:] for row in arr])


class TestPeakFinding2D(unittest.TestCase):
    def test_peak_finding_2d(self):
        # Test with a 3x3 array with a peak at the center
        arr = [ [ 1, 2, 3 ], 
                [ 4, 5, 6 ], 
                [ 7, 8, 9 ] ]
        self.assertEqual(peak_finding_2d(arr), 9)

        # Test with a 3x3 array with a peak at the corner
        arr = [ [ 10, 8, 6 ], 
                [ 9, 7, 5 ], 
                [ 8, 6, 4 ] ]
        self.assertEqual(peak_finding_2d(arr), 10)

        # Test with a 4x4 array with a peak at the edge
        arr = [ [ 10, 8, 10, 10 ], 
                [ 14, 13, 12, 11 ], 
                [ 15, 11, 4, 10 ], 
                [ 16, 17, 19, 20 ] ]
        self.assertEqual(peak_finding_2d(arr), 20)


if __name__ == '__main__':
    unittest.main()
