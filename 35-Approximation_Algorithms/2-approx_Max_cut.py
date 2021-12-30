import random
from collections import defaultdict

"""
Optimization problem Max Cut: given an undirected graph G = (V, E), find L ⊆ V maximizing1
|δ(L)|. If we can solve this in polynomial time, then we can solve the decision problem just mentioned in
polynomial time which would then mean P = NP.
"""
# Function to build the graph
def build_graph():
    edges = [
        ["A", "B"], ["A", "E"],
        ["A", "C"], ["B", "D"],
        ["B", "E"], ["C", "F"],
        ["C", "G"], ["D", "E"]
    ]
    graph = defaultdict(list) 
    # Loop to iterate over every
    # edge of the graph
    for edge in edges:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph

def max_cut():
    # initialize the random seed
    random.seed(1)
    graph = build_graph()
    L = []
    # Loop to iterate over every node
    for node in graph:
        # random choice ( if 1 we include the node in our delta(L) 
        # to maximise the cut)
        choice = random.choice([0,1])
        if choice == 1:
            L.append(node)
    return L

print(max_cut())
    