import unittest

# Author: Robert Joseph

def activity_selection(s, f):
    """
    This function implements the activity selection algorithm, which selects
    a maximum set of mutually compatible activities given their start times
    and finish times.
    """
    n = len(s)
    t = set()
    i = 0
    j = 0

    while j < n:
        if s[j] >= f[i]:
            t.add(j)  # add the current activity index to the set
            i = j
        j += 1
    
    return t


class TestActivitySelection(unittest.TestCase):
    def test_activity_selection(self):
        # Test case 1: Activities [0, 2, 4] are selected
        s = [1, 3, 0, 5, 8, 5]
        f = [2, 4, 6, 7, 9, 9]
        self.assertEqual(activity_selection(s, f), {0, 2, 4})

        # Test case 2: Activities [0, 3] are selected
        s = [1, 2, 3, 4, 5]
        f = [3, 4, 5, 6, 7]
        self.assertEqual(activity_selection(s, f), {0, 3})

        # Test case 3: Activities [1, 4, 5] are selected
        s = [1, 2, 4, 5, 7, 9]
        f = [3, 4, 6, 7, 9, 10]
        self.assertEqual(activity_selection(s, f), {1, 4, 5})


if __name__ == '__main__':
    unittest.main()
