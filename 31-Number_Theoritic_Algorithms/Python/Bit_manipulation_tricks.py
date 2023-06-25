import unittest

# Author: Robert Joseph

def reverse(A):
    """
    Reverses the bits of an integer A.
    """
    # Convert A to binary representation with 32 bits
    binary = "{:032b}".format(A)
    
    # Reverse the binary representation and convert it back to an integer
    reversed_binary = binary[::-1]
    return int(reversed_binary, 2)


def count_1(A):
    """
    Counts the number of 1 bits in an integer A.
    """
    count = 0
    while A:
        A &= (A-1)
        count += 1
    return count


def count_0(A):
    """
    Counts the number of 0 bits in an integer A.
    """
    binary = "{:032b}".format(A)
    return binary.count("0")


def set_bit(A, i):
    """
    Sets the i-th bit of an integer A to 1.
    """
    return A | (1 << i)


def get_bit(A, i):
    """
    Returns the value of the i-th bit of an integer A.
    """
    return A & (1 << i)


def swap(a, b):
    """
    Swaps the values of two numbers using bit manipulation.
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


def even(A):
    """
    Checks if an integer A is even or odd.
    """
    return (A & 1) == 0


def clear_bit(A, i):
    """
    Clears the i-th bit of an integer A (sets it to 0).
    """
    return A & ~(1 << i)


def add(a, b):
    """
    Adds two binary numbers a and b.
    """
    # Convert a and b to binary representations with 32 bits
    l = "{:032b}".format(a)
    m = "{:032b}".format(b)

    # Perform bitwise addition
    j = ""
    for i in range(32):
        j = j + str(int(l[i]) + int(m[i]))

    # Print or return the result

    # Note: The original code does not print or return the result, so you might want
    # to modify it accordingly. For example, you can return the integer representation
    # of the binary sum:
    return int(j, 2)


def single_1(A):
    """
    Finds the integer that occurs only once in a list A where all other integers
    occur three times.
    """
    # Initialize a binary representation of 0
    l = "{:032b}".format(0)
    l = [int(i) for i in l]

    # Iterate over each integer in A
    for i in A:
        m = "{:032b}".format(i)

        # Add the binary representations bit by bit
        for k in range(32):
            l[k] = str(int(l[k]) + int(m[k]))

    # Find the remainder when each bit is divided by 3
    for i in range(len(l)):
        l[i] = str(int(l[i]) % 3)

    # Convert the binary representation back to an integer
    return int("".join(l), 2)


class TestBitManipulation(unittest.TestCase):
    def test_reverse(self):
        # Test reversing bits of a positive integer
        self.assertEqual(reverse(10), 1342177280)

        # Test reversing bits of a negative integer
        self.assertEqual(reverse(-10), -1610612736)

    def test_count_1(self):
        # Test counting 1 bits in a positive integer
        self.assertEqual(count_1(10), 2)

        # Test counting 1 bits in a negative integer
        self.assertEqual(count_1(-10), 30)

    def test_count_0(self):
        # Test counting 0 bits in a positive integer
        self.assertEqual(count_0(10), 30)

        # Test counting 0 bits in a negative integer
        self.assertEqual(count_0(-10), 2)


if __name__ == '__main__':
    unittest.main()
