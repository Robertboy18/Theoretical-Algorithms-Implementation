import unittest

# Author: Robert Joseph

def pi_array(pattern):
    """
    Compute the pi[] values for the pattern using the KMP algorithm.
    Time complexity: O(|p|)
    """
    pi = [0] * len(pattern)
    for i in range(1, len(pattern)):
        j = pi[i - 1]
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            pi[i] = j + 1
    return pi

def KMP(text, pattern):
    """
    Perform string matching using the KMP algorithm.
    Time complexity: O(|s|)
    """
    pi = pi_array(pattern)
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            return i - len(pattern) + 1
    return -1


class TestKMP(unittest.TestCase):
    def test_KMP(self):
        text = "abcdefghij"
        pattern = "def"
        self.assertEqual(KMP(text, pattern), 3)

        text = "aabbaabbaabb"
        pattern = "aabbaabb"
        self.assertEqual(KMP(text, pattern), 4)

        text = "banana"
        pattern = "nan"
        self.assertEqual(KMP(text, pattern), 2)


if __name__ == '__main__':
    unittest.main()
