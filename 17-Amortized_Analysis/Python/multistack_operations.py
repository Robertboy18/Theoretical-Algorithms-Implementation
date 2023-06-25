import unittest

# Author: Robert Joseph

def multipop(S, k):
    """
    This generator function yields the top k elements from the stack S,
    removing them from the stack in the process.
    """
    while k > 0 and S:
        yield S.pop()
        k -= 1

def multipush(S, k):
    """
    This function pushes the value k onto the stack S k times.
    """
    for _ in range(k):
        S.append(k)

# Unit tests for multipop and multipush functions
class TestStackOperations(unittest.TestCase):
    def test_multipop(self):
        S = [1, 2, 3, 4, 5]
        k = 2
        result = list(multipop(S, k))
        self.assertEqual(result, [5, 4])
        self.assertEqual(S, [1, 2, 3])

        S = [1, 2, 3, 4, 5]
        k = 5
        result = list(multipop(S, k))
        self.assertEqual(result, [5, 4, 3, 2, 1])
        self.assertEqual(S, [])

        S = [1, 2, 3, 4, 5]
        k = 10
        result = list(multipop(S, k))
        self.assertEqual(result, [5, 4, 3, 2, 1])
        self.assertEqual(S, [])

    def test_multipush(self):
        S = []
        k = 3
        multipush(S, k)
        self.assertEqual(S, [3, 3, 3])

        S = [1, 2, 3]
        k = 0
        multipush(S, k)
        self.assertEqual(S, [1, 2, 3])

        S = []
        k = 1
        multipush(S, k)
        self.assertEqual(S, [1])

if __name__ == '__main__':
    unittest.main()
