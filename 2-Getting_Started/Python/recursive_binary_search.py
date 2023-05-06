import unittest

# Author: Robert Joseph

def binary_search(arr, l, r, x):
    """
    This function implements the binary search algorithm to search for an
    element x in a sorted array arr[l...r].
    """
    if r >= l:
        # calculate the middle index of the array
        mid = l + (r - l) // 2
        
        if arr[mid] == x:
            # if the middle element is equal to x, return True
            return True
        
        elif arr[mid] > x:
            # if the middle element is greater than x, search the left half of the array
            return binary_search(arr, l, mid-1, x)
        
        else:
            # if the middle element is less than x, search the right half of the array
            return binary_search(arr, mid+1, r, x)
    
    else:
        # if the search has reached the end of the array without finding x, return False
        return False


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        # Test with an array of odd length
        arr = [2, 3, 4, 5, 6, 7, 8]
        x = 7
        self.assertTrue(binary_search(arr, 0, len(arr)-1, x))
        
        # Test with an array of even length
        arr = [2, 3, 4, 5, 6, 7]
        x = 4
        self.assertTrue(binary_search(arr, 0, len(arr)-1, x))
        
        # Test with an element not in the array
        arr = [2, 3, 4, 5, 6, 7]
        x = 8
        self.assertFalse(binary_search(arr, 0, len(arr)-1, x))


if __name__ == '__main__':
    unittest.main()
