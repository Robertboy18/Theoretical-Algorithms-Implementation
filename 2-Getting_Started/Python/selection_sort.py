import unittest

# Author: Robert Joseph

def selection(z):
    """
    This function sorts a given list z using selection sort algorithm,
    which repeatedly selects the minimum element from the unsorted part
    of the list and places it at the beginning of the sorted part.
    """
    # iterate over each element of the list
    for i in range(0, len(z)-1):
        # assume the current element is the minimum
        k = i
        # iterate over the remaining unsorted elements
        for j in range(i+1, len(z)):
            # if we find a smaller element, update the minimum index
            if z[j] < z[k]:
                k = j
        # swap the minimum element with the current element
        z[i], z[k] = z[k], z[i]
    # return the sorted list
    return z


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        # Test with a sorted list
        z = [1, 2, 3, 4, 5]
        self.assertEqual(selection(z), [1, 2, 3, 4, 5])

        # Test with a reverse sorted list
        z = [5, 4, 3, 2, 1]
        self.assertEqual(selection(z), [1, 2, 3, 4, 5])

        # Test with a random list
        z = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(selection(z), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])


if __name__ == '__main__':
    unittest.main()
