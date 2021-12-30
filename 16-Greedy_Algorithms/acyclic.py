# Original Author : Professor Zacharry Frigstad

# maximum-weight acyclic subgraph
# running time: O(|V| + |E| log |E|)

# union-find note: We are NOT using union-find by rank. Just path compression
# it simplifies the code a lot and, according to the textbook (union-find section)
# the total running time will still be O(|E| log |E|).

# find the representative of the component with v
def find(v, uf):
    if uf[v] != v: uf[v] = find(uf[v], uf)
    return uf[v]

# merge the two components containing u,v respectively
# returns True if they were in different components and there
# was an actual merger, false otherwise
def merge(u, v, uf):
    u, v = find(u, uf), find(v, uf)
    if u == v: return False
    uf[u] = v
    return True

if __name__ == "__main__":
    n, m = map(int, input().split())
    # an edge is a triple (u,v,w) where {u,v} is the edge
    # being modelled and w is its weight
    edges = list(tuple(map(int, input().split())) for i in range(m))

    # sort by weight
    edges.sort(key = lambda x : x[2])

    # assumes vertices are 1, ..., n
    uf = {i:i for i in range(1, n+1)}

    solution = []
    tot = 0
    for u, v, w in edges[::-1]:
        if merge(u, v, uf):
            solution.append((u,v,w))
            tot += w
    for u, v, w in solution:
        print("{0}, {1} - {2}".format(u, v, w))
    print("Maximum acyclic subgraph weight:", tot)
