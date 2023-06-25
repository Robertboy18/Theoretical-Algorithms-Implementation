import unittest

# Author: Robert Joseph

# Single Number using bit manipulation
# Time complexity: O(N)
# Space complexity: O(1)
def single_1(nums):
    # Create a list of 32 bits initialized to 0
    bit_count = [0] * 32
    
    # Count the number of set bits for each bit position
    for num in nums:
        # Convert the absolute value of the number to a binary string
        binary = "{:032b}".format(abs(num))
        
        # Iterate over each bit position
        for i in range(32):
            # Add the absolute value of the bit to the corresponding position in bit_count
            bit_count[i] += abs(int(binary[i]))
    
    # Take the modulo 3 of each bit count to determine the bits of the single number
    for i in range(32):
        bit_count[i] %= 3
    
    # Convert the bit count list to an integer
    single_num = int("".join(map(str, bit_count)), 2)
    
    # Check if the single number is positive or negative based on its count in the original list
    if nums.count(single_num) == 1:
        return single_num
    else:
        return -single_num


# Single Number using dictionary
# Time complexity: O(N)
# Space complexity: O(N)
def single_2(nums):
    count_dict = {}
    
    # Count the occurrences of each number using a dictionary
    for num in nums:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1
    
    # Find the number with count 1, which is the single number
    for num, count in count_dict.items():
        if count == 1:
            return num


class TestSingleNumber(unittest.TestCase):
    def test_single_1(self):
        nums = [1, 1, 2, 2, 3]
        self.assertEqual(single_1(nums), 3)

    def test_single_2(self):
        nums = [1, 1, 2, 2, 3]
        self.assertEqual(single_2(nums), 3)

    def test_single_3(self):
        nums = [4, 2, 2, 2, 4]
        self.assertEqual(single_2(nums), 4)


if __name__ == '__main__':
    unittest.main()
