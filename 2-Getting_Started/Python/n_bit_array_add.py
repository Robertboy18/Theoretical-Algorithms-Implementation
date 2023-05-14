import unittest

# Author: Robert Joseph

def bit_add(x, y):
    """
    This function performs binary addition on two bit strings x and y.
    It returns a new bit string that represents the sum of x and y.
    """
    # make sure x is the longer bit string
    if len(y) > len(x):
        x, y = y, x

    # initialize the result bit string with a zero at the end
    z = [0] * (len(x) + 1)
    c = 0  # carry bit
    
    # iterate over the bits of x and y
    for i in range(len(x)):
        # get the bit values of x and y, or 0 if out of range
        xi = x[-i-1] if i < len(x) else 0
        yi = y[-i-1] if i < len(y) else 0
        
        # compute the sum and carry bits
        c, z[-i-1] = divmod(xi + yi + c, 2)
    
    # set the last bit of the result to the carry bit
    z[0] = c
    
    # remove leading zeros
    while len(z) > 1 and z[0] == 0:
        z = z[1:]
    
    return z


class TestBitAdd(unittest.TestCase):
    def test_bit_add(self):
        # Test with bit strings 101 and 111
        a = [1, 0, 1]
        b = [1, 1, 1]
        self.assertEqual(bit_add(a, b), [1, 1, 0, 0])

        # Test with bit strings 1100 and 101
        a = [1, 1, 0, 0]
        b = [1, 0, 1]
        self.assertEqual(bit_add(a, b), [1, 0, 0, 0, 1])
        
        # Test with bit strings 1010 and 1010
        a = [1, 0, 1, 0]
        b = [1, 0, 1, 0]
        self.assertEqual(bit_add(a, b), [1, 0, 1, 0, 0])


if __name__ == '__main__':
    unittest.main()
