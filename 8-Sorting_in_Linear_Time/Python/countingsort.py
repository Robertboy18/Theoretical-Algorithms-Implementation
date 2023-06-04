import unittest

# Author: Robert Joseph

def counting_sort(arr):
    """
    This function implements counting sort to sort the input array in ascending order.
    Complexity: O(N+K), where N is the length of the array and K is the range of input values.
    """
    # Create a dictionary to store the count of each element
    count = dict()

    # Initialize the count for each element to 0
    for i in range(len(arr)):
        count[i] = 0

    # Count the occurrences of each element
    for j in range(len(arr)):
        count[arr[j]] += 1

    # Build the final sorted array by repeating each element according to its count
    final = ""
    for key, value in count.items():
        final += str(key) * value

    # Convert the final string into a list of integers
    final = [int(i) for i in final]

    return final


class TestCountingSort(unittest.TestCase):
    def test_counting_sort(self):
        # Test with positive integers
        arr = [3, 4, 3, 2, 4]
        sorted_arr = counting_sort(arr)
        self.assertEqual(sorted_arr, [2, 3, 3, 4, 4])

        # Test with negative integers
        arr = [-5, -2, -4, -3, -1]
        sorted_arr = counting_sort(arr)
        self.assertEqual(sorted_arr, [-5, -4, -3, -2, -1])

        # Test with mixed positive and negative integers
        arr = [4, -2, 0, -3, 1]
        sorted_arr = counting_sort(arr)
        self.assertEqual(sorted_arr, [-3, -2, 0, 1, 4])


if __name__ == '__main__':
    unittest.main()
