import unittest

# Author: Robert Joseph

def find_min_max(lst):
    """
    This function finds the minimum and maximum values in a list of numbers.
    It iterates through the list and updates the min and max values accordingly.
    """
    # Initialize min and max to the first element of the list
    min_val = lst[0]
    max_val = lst[0]

    # Iterate through the list, updating min and max as needed
    for num in lst:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    # Return the min and max values
    return min_val, max_val


class TestFindMinMax(unittest.TestCase):
    def test_find_min_max(self):
        # Test with a list of positive numbers
        lst = [3, 2, 1, 5, 4, 6, 7, 8, 9, 10]
        self.assertEqual(find_min_max(lst), (1, 10))

        # Test with a list of negative numbers
        lst = [-5, -3, -2, -8, -1]
        self.assertEqual(find_min_max(lst), (-8, -1))

        # Test with a list containing both positive and negative numbers
        lst = [4, -2, 6, -9, 0, 3]
        self.assertEqual(find_min_max(lst), (-9, 6))


if __name__ == '__main__':
    unittest.main()
