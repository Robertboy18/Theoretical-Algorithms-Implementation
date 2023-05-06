import unittest

# Author: Robert Joseph

def plusOne(A):
    """
    This function takes a non-negative integer represented as an array of digits
    and returns the integer plus one in the same format.
    
    The time complexity of this function is O(n), where n is the length of the input array A. This is because the function iterates over each digit in the array at most once.
    """
    c = 0
    t = -1
    choice = True
    while choice:
        c = A[t] % 10
        if c == 9 and len(A) == -t:
            # if the last digit is 9 and we've reached the left end of the array,
            # insert a new digit 1 at the beginning of the array
            A.insert(0,1)
            choice = False
        elif c != 9:
            # if the last digit is not 9, simply add 1 to it and exit the loop
            A[t] += 1
            choice = False
        else:
            # if the last digit is 9, set it to 0 and continue with the next digit
            A[t] = 0
            t = t - 1

    # remove leading zeros
    for i in range(len(A)):
        if A[i] != 0:
            return A[i:]
    return A


class TestPlusOne(unittest.TestCase):
    def test_plus_one(self):
        # test with input [0, 0, 1]
        A = [0, 0, 1]
        self.assertEqual(plusOne(A), [0, 0, 2])

        # test with input [1, 2, 3]
        A = [1, 2, 3]
        self.assertEqual(plusOne(A), [1, 2, 4])

        # test with input [9, 9, 9]
        A = [9, 9, 9]
        self.assertEqual(plusOne(A), [1, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
