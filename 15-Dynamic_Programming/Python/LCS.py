import unittest

# Author: Robert Joseph

def LCS_recursive(x, y, i, j):
    """
    This function calculates the length of the Longest Common Subsequence (LCS)
    between two strings x and y using a recursive approach.
    Time complexity: O(2^n)
    """
    if i == 0 or j == 0:
        return 0
    elif x[i-1] == y[j-1]:
        return 1 + LCS_recursive(x, y, i-1, j-1)
    else:
        return max(LCS_recursive(x, y, i, j-1), LCS_recursive(x, y, i-1, j))


def LCS_dp(x, y):
    """
    This function calculates the length of the Longest Common Subsequence (LCS)
    between two strings x and y using dynamic programming.
    Time complexity: O(len(x) * len(y))
    """
    dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
    for i in range(len(x) + 1):
        for j in range(len(y) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len(x)][len(y)]


class TestLCS(unittest.TestCase):
    def test_LCS_recursive(self):
        # Test with strings "abc" and "ab"
        x = "abc"
        y = "ab"
        self.assertEqual(LCS_recursive(x, y, len(x), len(y)), 2)

        # Test with strings "AGGTAB" and "GXTXAYB"
        x = "AGGTAB"
        y = "GXTXAYB"
        self.assertEqual(LCS_recursive(x, y, len(x), len(y)), 4)

        # Test with strings "abcdef" and "abcdef"
        x = "abcdef"
        y = "abcdef"
        self.assertEqual(LCS_recursive(x, y, len(x), len(y)), 6)

    def test_LCS_dp(self):
        # Test with strings "abc" and "ab"
        x = "abc"
        y = "ab"
        self.assertEqual(LCS_dp(x, y), 2)

        # Test with strings "AGGTAB" and "GXTXAYB"
        x = "AGGTAB"
        y = "GXTXAYB"
        self.assertEqual(LCS_dp(x, y), 4)

        # Test with strings "abcdef" and "abcdef"
        x = "abcdef"
        y = "abcdef"
        self.assertEqual(LCS_dp(x, y), 6)


if __name__ == '__main__':
    unittest.main()
