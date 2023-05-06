import unittest

# Author: Robert Joseph

def binary_search(z, x, low, high):
    """
    This function performs binary search on a sorted array z to find the index
    of the element x. If x is found, it returns True, otherwise it returns False.
    """
    while low <= high:
        # calculate the middle index
        mid = (low + high) // 2
        
        # check if the middle element is equal to x
        if z[mid] == x:
            return True
        
        # if x is less than the middle element, search the left half of the array
        elif z[mid] > x:
            high = mid - 1
        
        # if x is greater than the middle element, search the right half of the array
        else:
            low = mid + 1
    
    # x was not found in the array
    return False


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        # Test with an element that is in the array
        z = [-232, 1, 5, 5, 6, 7, 8, 24, 35, 67]
        x = 5
        self.assertTrue(binary_search(z, x, 0, len(z) - 1))
        
        # Test with an element that is not in the array
        x = 23
        self.assertFalse(binary_search(z, x, 0, len(z) - 1))
        
        # Test with an empty array
        z = []
        x = 42
        self.assertFalse(binary_search(z, x, 0, len(z) - 1))


if __name__ == '__main__':
    unittest.main()
