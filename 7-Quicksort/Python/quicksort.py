import unittest

# Author: Robert Joseph

def partition(A, low, high):
    """
    This function selects a pivot element from the array A[low:high+1]
    and rearranges the elements such that all elements smaller than or equal
    to the pivot are placed before it, and all elements greater than the pivot
    are placed after it. It returns the index of the pivot.
    """
    pivot = A[high]
    i = low - 1
    j = low
    while j < high:
        if A[j] <= pivot:
            i += 1
            A[j], A[i] = A[i], A[j]
        j += 1
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1

def quicksort(A, low, high):
    """
    This function implements the QuickSort algorithm to sort the array A[low:high+1].
    It recursively partitions the array based on a pivot element and sorts the partitions.
    """
    if low < high:
        part = partition(A, low, high)
        quicksort(A, low, part - 1)
        quicksort(A, part + 1, high)

# Unit tests
class TestQuickSort(unittest.TestCase):
    def test_quicksort(self):
        # Test with positive integers
        A = [10, 80, 30, 90, 40, 50, 70]
        quicksort(A, 0, len(A) - 1)
        self.assertEqual(A, [10, 30, 40, 50, 70, 80, 90])

        # Test with negative integers
        A = [-10, -80, -30, -90, -40, -50, -70]
        quicksort(A, 0, len(A) - 1)
        self.assertEqual(A, [-90, -80, -70, -50, -40, -30, -10])

        # Test with mixed positive and negative integers
        A = [-10, 80, -30, 90, -40, 50, -70]
        quicksort(A, 0, len(A) - 1)
        self.assertEqual(A, [-70, -40, -30, -10, 50, 80, 90])

if __name__ == '__main__':
    unittest.main()