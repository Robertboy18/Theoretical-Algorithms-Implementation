import unittest

# Author: Robert Joseph

def on_line_maximum(k, n, score):
    """
    This function finds the index of the first occurrence of the maximum value
    of the score list, starting from index k and ending at index n-1.
    """
    # initialize the best score to a very low value
    bestscore = -10e10
    
    # iterate over the first k elements of the score list
    for i in range(k):
        # if the current element is greater than the best score so far,
        # update the best score
        if score[i] > bestscore:
            bestscore = score[i]
    
    # iterate over the remaining elements of the score list
    for i in range(k+1, n):
        # if the current element is greater than the best score so far,
        # return the current index
        if score[i] > bestscore:
            return i
    
    # if no element after index k is greater than the best score, return n
    return n

class TestOnLineMaximum(unittest.TestCase):
    def test_on_line_maximum(self):
        # Test with score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(on_line_maximum(3, 10, score), 9)

        # Test with score = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        score = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(on_line_maximum(0, 10, score), 0)

        # Test with score = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
        score = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
        self.assertEqual(on_line_maximum(5, 10, score), 4)


if __name__ == '__main__':
    unittest.main()
