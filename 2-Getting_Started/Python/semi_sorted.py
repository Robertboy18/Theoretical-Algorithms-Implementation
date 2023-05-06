import unittest

# Author: Robert Joseph

def semi_sorted(arr, f, l):
    """
    This function finds the peak element in a semi-sorted array using binary search.
    A semi-sorted array is an array in which every element is at most k positions away from its sorted position.
    """
    # base case: array of size 1
    if f == l:
        return arr[f]
    
    # calculate mid index
    mid = (f + l)//2
    
    # check if mid is the peak element
    if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
        return arr[mid]
    
    # if mid is not the peak element, recurse on the subarray with higher values
    if arr[mid] > arr[mid + 1]:
        return semi_sorted(arr, f, mid)
    else:
        return semi_sorted(arr, mid + 1, l)


class TestSemiSorted(unittest.TestCase):
    def test_semi_sorted(self):
        # Test with a peak at the beginning of the array
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(semi_sorted(arr, 0, len(arr)-1), 10)

        # Test with a peak at the end of the array
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(semi_sorted(arr, 0, len(arr)-1), 10)

        # Test with a peak in the middle of the array
        arr = [1, 2, 3, 4, 9, 7, 6, 5, 4, 3]
        self.assertEqual(semi_sorted(arr, 0, len(arr)-1), 9)


if __name__ == '__main__':
    unittest.main()
