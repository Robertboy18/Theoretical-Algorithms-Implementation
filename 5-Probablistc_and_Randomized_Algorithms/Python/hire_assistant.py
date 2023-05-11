import random 
import unittest

# Author: Robert Joseph

def randomized_hire_assistant(n):
    """
    This function simulates the hiring process of an assistant,
    where n candidates are interviewed and ranked in random order.
    The function uses a variant of the "hire assistant" algorithm,
    where each candidate is hired if and only if they are the best
    seen so far, and the goal is to minimize the number of hires.
    The algorithm has an expected hiring cost of O(log n) per candidate.
    """
    # create a list of candidates with random rankings
    A = [i for i in range(n)]
    random.shuffle(A)
    print("Candidates are (rankings):", A)
    
    # hire the first candidate and initialize the best seen so far
    best = 0
    times = 0
    for i in range(1, n):
        # if the current candidate is better than the best seen so far, hire them
        if A[i] > A[best]:
            times += 1
            best = i
    
    # return the number of times a candidate was hired
    return times


class TestRandomizedHireAssistant(unittest.TestCase):
    def test_randomized_hire_assistant(self):
        # Test with n=1
        n = 1
        self.assertEqual(randomized_hire_assistant(n), 0)

        # Test with n=5
        n = 5
        self.assertLessEqual(randomized_hire_assistant(n), 2)

        # Test with n=10
        n = 10
        self.assertLessEqual(randomized_hire_assistant(n), 4)


if __name__ == '__main__':
    unittest.main()
