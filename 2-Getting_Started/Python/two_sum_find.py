import unittest

# Author: Robert Joseph

def binary_search(arr, x):
    """
    This function implements the binary search algorithm to search for a
    given element x in a sorted array arr.
    """
    # initialize the search range
    l, r = 0, len(arr) - 1
    
    # loop until the search range is exhausted
    while l <= r:
        # compute the midpoint of the search range
        mid = (l + r) // 2
        
        # check if the midpoint is the element we're looking for
        if arr[mid] == x:
            return True
        
        # if the midpoint is greater than the element we're looking for,
        # search the left half of the search range
        elif arr[mid] > x:
            r = mid - 1
        
        # if the midpoint is less than the element we're looking for,
        # search the right half of the search range
        else:
            l = mid + 1
    
    # if we haven't found the element by this point, it's not in the array
    return False


def sum_find(arr, x):
    """
    This function checks whether there are two elements in a given array
    whose sum is equal to a given value x.
    """
    # sort the array in non-decreasing order
    arr.sort()
    
    # iterate over each element in the array
    for i in range(len(arr)):
        # check if there is another element in the array whose value
        # is equal to x minus the current element
        if binary_search(arr, x - arr[i]):
            return True
    
    # if we haven't found a pair of elements whose sum is x by this point,
    # there aren't any such pairs in the array
    return False


class TestSumFind(unittest.TestCase):
    def test_sum_find(self):
        # Test with array [1, 2, 54, 699]
        a = [1, 2, 54, 699]
        self.assertTrue(sum_find(a, 3))
        self.assertFalse(sum_find(a, 5))
        self.assertTrue(sum_find(a, 701))


if __name__ == '__main__':
    unittest.main()
