import unittest

# Author: Robert Joseph

def insertion_sort(d):
    """
    This function implements the insertion sort algorithm, which sorts
    a list of numbers d in ascending order.
    """
    # iterate over each element of the list, starting from the second element
    for i in range(1, len(d)):
        # store the current element in a variable
        key = d[i]
        
        # compare the current element with the previous elements in the list
        j = i - 1
        while j >= 0 and key < d[j]:
            # if the current element is smaller than the previous element,
            # move the previous element one position to the right
            d[j+1] = d[j]
            j -= 1
        
        # insert the current element in its correct position in the sorted list
        d[j+1] = key
    
    # return the sorted list
    return d


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        # Test with a list of random integers
        d = [5, 2, 8, 1, 3]
        self.assertEqual(insertion_sort(d), [1, 2, 3, 5, 8])

        # Test with an already sorted list
        d = [1, 2, 3, 4, 5]
        self.assertEqual(insertion_sort(d), [1, 2, 3, 4, 5])

        # Test with a list of repeated elements
        d = [5, 5, 5, 5, 5]
        self.assertEqual(insertion_sort(d), [5, 5, 5, 5, 5])


if __name__ == '__main__':
    unittest.main()
