import unittest

# Author: Robert Joseph

def insertion_sort(d):
    """
    This function implements the insertion sort algorithm to sort
    a list of numbers in descending order.
    """
    # iterate over each element in the list
    for i in range(1, len(d)):
        key = d[i]
        j = i - 1
        # move elements that are greater than the key to the right
        while j >= 0 and key > d[j]:
            d[j + 1] = d[j]
            j -= 1
        # insert the key in its correct position
        d[j + 1] = key
    # return the sorted list
    return d


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        # Test with a list of random integers
        d = [4, 6, 3, 1, 5, 2]
        self.assertEqual(insertion_sort(d), [6, 5, 4, 3, 2, 1])

        # Test with a list of descending integers
        d = [6, 5, 4, 3, 2, 1]
        self.assertEqual(insertion_sort(d), [6, 5, 4, 3, 2, 1])

        # Test with a list of ascending integers
        d = [1, 2, 3, 4, 5, 6]
        self.assertEqual(insertion_sort(d), [6, 5, 4, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
