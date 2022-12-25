class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def dfs(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in range(self.vertices):
            if self.graph[v][i] == 1 and visited[i] is False:
                self.dfs(i, visited)

    def dfs_traversal(self, v):
        visited = [False] * self.vertices
        self.dfs(v, visited)


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.dfs_traversal(2)