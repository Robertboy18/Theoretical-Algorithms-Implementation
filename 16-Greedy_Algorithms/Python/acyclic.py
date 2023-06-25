# Original Author : Professor Zacharry Frigstad

# maximum-weight acyclic subgraph
# running time: O(|V| + |E| log |E|)

# union-find note: We are NOT using union-find by rank. Just path compression
# it simplifies the code a lot and, according to the textbook (union-find section)
# the total running time will still be O(|E| log |E|).

import unittest

# find the representative of the component with v
def find(v, uf):
    """
    Find the representative of the component that contains vertex v.
    Uses path compression to optimize future find operations.
    """
    if uf[v] != v:
        uf[v] = find(uf[v], uf)
    return uf[v]

# merge the two components containing u, v respectively
# returns True if they were in different components and there
# was an actual merger, false otherwise
def merge(u, v, uf):
    """
    Merge the components containing vertices u and v.
    Returns True if the vertices were in different components and a merger occurred,
    False otherwise.
    """
    u, v = find(u, uf), find(v, uf)
    if u == v:
        return False
    uf[u] = v
    return True

def maximum_acyclic_subgraph_weight(n, m, edges):
    """
    Finds the maximum weight acyclic subgraph using Kruskal's algorithm.
    Returns the total weight of the subgraph and the list of selected edges.
    """

    # Sort edges by weight in non-decreasing order
    edges.sort(key=lambda x: x[2])

    # Initialize union-find data structure
    uf = {i: i for i in range(1, n + 1)}

    solution = []
    total_weight = 0

    # Iterate over edges in reverse order (largest weight first)
    for u, v, w in edges[::-1]:
        if merge(u, v, uf):
            solution.append((u, v, w))
            total_weight += w

    return total_weight, solution


class TestMaximumAcyclicSubgraph(unittest.TestCase):
    def test_maximum_acyclic_subgraph(self):
        # Test case 1
        n = 5
        m = 7
        edges = [(1, 2, 2), (2, 3, 3), (1, 3, 4), (3, 4, 5), (4, 5, 1), (3, 5, 6), (2, 5, 7)]
        weight, selected_edges = maximum_acyclic_subgraph_weight(n, m, edges)
        self.assertEqual(weight, 14)
        self.assertEqual(selected_edges, [(2, 5, 7), (3, 5, 6), (4, 5, 1)])

        # Test case 2
        n = 4
        m = 5
        edges = [(1, 2, 2), (1, 3, 3), (2, 3, 1), (3, 4, 5), (2, 4, 4)]
        weight, selected_edges = maximum_acyclic_subgraph_weight(n, m, edges)
        self.assertEqual(weight, 7)
        self.assertEqual(selected_edges, [(2, 3, 1), (1, 3, 3), (3, 4, 5)])

        # Test case 3
        n = 3
        m = 3
        edges = [(1, 2, 1), (1, 3, 2), (2, 3, 3)]
        weight, selected_edges = maximum_acyclic_subgraph_weight(n, m, edges)
        self.assertEqual(weight, 3)
        self.assertEqual(selected_edges, [(1, 2, 1), (1, 3, 2)])

if __name__ == '__main__':
    unittest.main()