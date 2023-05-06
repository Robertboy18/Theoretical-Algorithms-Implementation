import unittest

# Author: Robert Joseph

def bubble_sort(arr):
    """
    This function implements the bubble sort algorithm to sort an array in ascending order.
    """
    # Iterate through the array for each element
    for i in range(len(arr)):
        # Compare each element with every other element
        for j in range(i+1, len(arr)):
            # Swap if the current element is greater than the next element
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        # Test with an unsorted array
        arr = [4, 2, 5, 1, 3]
        self.assertEqual(bubble_sort(arr), [1, 2, 3, 4, 5])

        # Test with an already sorted array
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), [1, 2, 3, 4, 5])

        # Test with a reversed sorted array
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(bubble_sort(arr), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
