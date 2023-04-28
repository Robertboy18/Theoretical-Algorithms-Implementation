from collections import defaultdict

# Function to find the maximum flow from source to sink
def fordFulkerson(graph, source, sink):
    # Residual graph where residualGraph[i][j] indicates residual capacity of edge i-j
    residualGraph = graph

    # Stores the parent of each vertex in the BFS tree
    parent = [-1] * len(graph)

    # Stores the maximum flow from source to sink
    maxFlow = 0

    # While there is a path from source to sink
    while bfs(residualGraph, source, sink, parent):
        # Find the minimum residual capacity along the path
        minResidualCapacity = float('inf')
        u = sink
        while u != source:
            minResidualCapacity = min(minResidualCapacity, residualGraph[parent[u]][u])
            u = parent[u]

        # Add the minimum flow to the maximum flow
        maxFlow += minResidualCapacity

        # Update the residual capacities along the path
        u = sink
        while u != source:
            residualGraph[parent[u]][u] -= minResidualCapacity
            residualGraph[u][parent[u]] += minResidualCapacity
            u = parent[u]

    return maxFlow

# Function to perform BFS to find the path from source to sink
def bfs(residualGraph, source, sink, parent):
    # Queue to store the vertices to be visited
    queue = []

    # Set all vertices as not visited
    visited = [False] * len(residualGraph)

    # Mark the source vertex as visited and enqueue it
    queue.append(source)
    visited[source] = True

    # Loop until queue is empty
    while queue:
        # Dequeue the first vertex from the queue
        u = queue.pop(0)

        # Loop through all the adjacent vertices of u
        for v in range(len(residualGraph)):
            # If the vertex is not visited and there is residual capacity
            if visited[v] == False and residualGraph[u][v] > 0:
                # Mark the vertex as visited and enqueue it
                queue.append(v)
                visited[v] = True
                parent[v] = u

    # Return True if there is a path from source to sink, otherwise False
    return True if visited[sink] else False

# Example graph
graph = defaultdict(dict)
graph[0][1] = 3
graph[0][2] = 2
graph[1][2] = 2
graph[1][3] = 1
graph[2][4] = 4
graph[3][4] = 3

# Find the minimum cut in the graph
minCut = fordFulkerson(graph, 0, 4)
print("Minimum cut:", minCut)
