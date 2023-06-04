import unittest
import collections

# Author: Robert Joseph

def dutch_flag(L):
    """
    This function sorts a list of elements containing 'R', 'W', and 'B'
    according to the Dutch national flag problem. The elements are rearranged
    so that all 'R' elements come before 'W' elements, and all 'W' elements
    come before 'B' elements.

    Time complexity: O(N), where N is the length of the list L.
    Space complexity: O(N) - Uses a dictionary to count occurrences of 'R', 'W', and 'B'.
    """
    counts = collections.Counter(L)
    sorted_list = []
    for color in ['R', 'W', 'B']:
        count = counts[color]
        sorted_list.extend([color] * count)
    return sorted_list


def dutch_flag1(L):
    """
    This function sorts a list of elements containing 'R', 'W', and 'B'
    according to the Dutch national flag problem. The elements are rearranged
    so that all 'R' elements come before 'W' elements, and all 'W' elements
    come before 'B' elements.

    Time complexity: O(N), where N is the length of the list L.
    Space complexity: O(1) - Rearranges the elements in-place.
    """
    r = L.count('R')
    w = L.count('W')
    b = L.count('B')
    for i in range(r):
        L[i] = 'R'
    for j in range(r, r+w):
        L[j] = 'W'
    for k in range(r+w, r+w+b):
        L[k] = 'B'
    return L


class TestDutchFlag(unittest.TestCase):
    def test_dutch_flag(self):
        # Test with list ['R', 'B', 'W', 'R', 'B', 'R', 'R']
        # Expected output: ['R', 'R', 'R', 'R', 'W', 'B', 'B']
        l = ['R', 'B', 'W', 'R', 'B', 'R', 'R']
        self.assertEqual(dutch_flag(l), ['R', 'R', 'R', 'R', 'W', 'B', 'B'])
        self.assertEqual(dutch_flag1(l), ['R', 'R', 'R', 'R', 'W', 'B', 'B'])

        # Test with list ['R', 'R', 'R']
        # Expected output: ['R', 'R', 'R']
        l = ['R', 'R', 'R']
        self.assertEqual(dutch_flag(l), ['R', 'R', 'R'])
        self.assertEqual(dutch_flag1(l), ['R', 'R', 'R'])

        # Test with list ['B', 'W']
        # Expected output: ['W', 'B']
        l = ['B', 'W']
        self.assertEqual(dutch_flag(l), ['W', 'B'])
        self.assertEqual(dutch_flag1(l), ['W', 'B'])


if __name__ == '__main__':
    unittest.main()
