import unittest

# Author: Robert Joseph


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        """
        Inserts a new node with the given value into the binary tree.
        Time complexity: O(log n) on average for a balanced tree,
                        O(n) in the worst case for a skewed tree.
        """
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current_node = self.root
        while True:
            if value <= current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                current_node = current_node.right

    def search(self, value):
        """
        Searches for a node with the given value in the binary tree.
        Returns True if found, False otherwise.
        Time complexity: O(log n) on average for a balanced tree,
                        O(n) in the worst case for a skewed tree.
        """
        current_node = self.root
        while current_node is not None:
            if value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False


class TestBinaryTree(unittest.TestCase):
    def test_binary_tree(self):
        # Test tree creation and search
        tree = BinaryTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(15)
        tree.insert(7)
        tree.insert(12)

        self.assertTrue(tree.search(10))  # Existing value in the tree
        self.assertTrue(tree.search(7))  # Existing value in the tree
        self.assertFalse(tree.search(20))  # Non-existing value in the tree


if __name__ == '__main__':
    unittest.main()
