import unittest

# Author: Robert Joseph

class Graph:
    def __init__(self, vertices):
        """
        This class represents a graph with 'vertices' number of vertices.
        """
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def add_edge(self, u, v):
        """
        This method adds an edge between vertices 'u' and 'v'.
        """
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def dfs(self, v, visited):
        """
        This method performs a Depth-First Search (DFS) traversal starting from vertex 'v'.
        It recursively explores the connected vertices in a depth-first manner.
        """
        visited[v] = True
        print(v, end=' ')

        for i in range(self.vertices):
            if self.graph[v][i] == 1 and not visited[i]:
                self.dfs(i, visited)

    def dfs_traversal(self, v):
        """
        This method initiates a DFS traversal starting from vertex 'v'.
        It keeps track of visited vertices and prints the traversal order.
        """
        visited = [False] * self.vertices
        self.dfs(v, visited)


class TestGraph(unittest.TestCase):
    def test_dfs_traversal(self):
        g = Graph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 3)

        # Test DFS traversal starting from vertex 2
        expected_output = "2 0 1 3"
        output = self.get_function_output(g.dfs_traversal, 2)
        self.assertEqual(output.strip(), expected_output)

        # Test DFS traversal starting from vertex 0
        expected_output = "0 1 2 3"
        output = self.get_function_output(g.dfs_traversal, 0)
        self.assertEqual(output.strip(), expected_output)

        # Test DFS traversal starting from vertex 3
        expected_output = "3 2 0 1"
        output = self.get_function_output(g.dfs_traversal, 3)
        self.assertEqual(output.strip(), expected_output)

    def get_function_output(self, function, *args):
        """
        Helper method to capture the output of a function.
        """
        from io import StringIO
        import sys

        # Redirect stdout to a StringIO object
        output = StringIO()
        sys.stdout = output

        # Call the function with the provided arguments
        function(*args)

        # Get the output value
        output_value = output.getvalue()

        # Restore stdout
        sys.stdout = sys.__stdout__

        return output_value


if __name__ == '__main__':
    unittest.main()
