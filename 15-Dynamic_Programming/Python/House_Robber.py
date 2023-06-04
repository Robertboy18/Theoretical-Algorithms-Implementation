import unittest

# Author: Robert Joseph

def house(nums):
    """
    This function calculates the maximum amount of money that can be robbed from a row of houses,
    where each house contains a certain amount of money. The adjacent houses cannot be robbed.
    It uses dynamic programming to find the maximum amount.
    """
    if len(nums) < 2:
        return nums[0]

    # Create a dynamic programming array to store the maximum amount at each house
    dp = [0] * len(nums)

    # Initialize the first two values of the dynamic programming array
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    # Iterate over the remaining houses and calculate the maximum amount at each house
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    # Return the maximum amount from the last house
    return dp[-1]


class TestHouseRobber(unittest.TestCase):
    def test_house_robber(self):
        # Test with nums = [1, 2, 3, 1]
        nums = [1, 2, 3, 1]
        self.assertEqual(house(nums), 4)

        # Test with nums = [2, 7, 9, 3, 1]
        nums = [2, 7, 9, 3, 1]
        self.assertEqual(house(nums), 12)

        # Test with nums = [2, 1, 1, 2]
        nums = [2, 1, 1, 2]
        self.assertEqual(house(nums), 4)


if __name__ == '__main__':
    unittest.main()
