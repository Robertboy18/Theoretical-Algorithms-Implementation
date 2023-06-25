import unittest
import collections as c

# Author: Robert Joseph

def knapsack_fractional(p, w, M):
    """
    This function solves the fractional knapsack problem, where we have a set
    of items with their respective values and weights, and we want to select
    items to maximize the total value within a given weight constraint.

    The function takes the following parameters:
    - p: A list of item values.
    - w: A list of item weights.
    - M: The maximum weight constraint.

    The function returns the maximum achievable value within the weight constraint.
    """
    # Create a dictionary to store the item values and weights ratios as keys
    # and their corresponding values and weights as values
    item_ratios = c.defaultdict(list)
    for i in range(len(p)):
        ratio = round(float(p[i] / w[i]), 2)
        item_ratios[ratio].append(p[i])
        item_ratios[ratio].append(w[i])
    
    # Sort the item ratios in descending order
    sorted_ratios = dict(sorted(item_ratios.items(), key=lambda x: x[0], reverse=True))
    
    # Initialize the final value
    final_value = 0
    
    # Iterate over the sorted ratios and select items greedily
    for _, v in sorted_ratios.items():
        if M - v[1] >= 0:
            # If the item can be fully included, add its value to the final value
            final_value += v[0]
            M -= v[1]
        else:
            # If the item cannot be fully included, include a fraction of it
            final_value += float(M / v[1]) * v[0]
            M -= int(v[0] - float(M / v[1]))
            break
    
    return final_value


class TestKnapsackFractional(unittest.TestCase):
    def test_knapsack_fractional(self):
        # Test case 1
        p = [25, 24, 15]
        w = [18, 15, 10]
        M = 20
        self.assertAlmostEqual(knapsack_fractional(p, w, M), 31.25)

        # Test case 2
        p = [50, 40, 30]
        w = [5, 4, 3]
        M = 10
        self.assertAlmostEqual(knapsack_fractional(p, w, M), 150)

        # Test case 3
        p = [10, 20, 30]
        w = [1, 2, 3]
        M = 5
        self.assertAlmostEqual(knapsack_fractional(p, w, M), 66.66666666666667)


if __name__ == '__main__':
    unittest.main()
