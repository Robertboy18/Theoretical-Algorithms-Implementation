import unittest

# Author: Robert Joseph

def art_gallery(x):
    """
    This function calculates the minimum number of guards required to secure
    an art gallery given the positions of the artwork along a wall.
    The function uses a greedy approach to minimize the number of guards needed.
    """
    # Sort the positions in ascending order
    # Time complexity: O(NlogN) due to sorting
    l = sorted(x)
    
    # Initialize the number of guards and the position of the previous artwork
    m = 1
    y = x[0]
    
    # Iterate over the sorted positions and check the distance between artworks
    # Time complexity: O(N)
    for i in range(1, len(x)):
        # If the distance between the current artwork and the previous one is greater than 1,
        # place a new guard and update the position of the previous artwork
        if abs(y - x[i]) > 1:
            m += 1
            y = x[i] + 1
    
    # Return the minimum number of guards required
    return m


class TestArtGallery(unittest.TestCase):
    def test_art_gallery(self):
        # Test with positions [1, 2, 3, 4]
        # Minimum number of guards required: 1
        x = [1, 2, 3, 4]
        self.assertEqual(art_gallery(x), 1)

        # Test with positions [1, 2, 4, 5]
        # Minimum number of guards required: 2
        x = [1, 2, 4, 5]
        self.assertEqual(art_gallery(x), 2)

        # Test with positions [1, 5, 9, 12, 15]
        # Minimum number of guards required: 3
        x = [1, 5, 9, 12, 15]
        self.assertEqual(art_gallery(x), 3)


if __name__ == '__main__':
    unittest.main()
