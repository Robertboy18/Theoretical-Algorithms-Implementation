import random
from collections import defaultdict
import networkx as nx

"""
The vertex-cover problem is to find a vertex cover of minimum size in a given
undirected graph. We call such a vertex cover an optimal vertex cover. 
This problem is the optimization version of an NP-complete decision problem
"""

def build_graph():
    G = nx.Graph()
    G.add_nodes_from([1,2,3,4])
    G.add_edges_from([(1, 2),(1, 3),(2,4),(3,4)])
    return G
    
def vertex_cover():
    # initialize the random seed
    random.seed(1)
    graph = build_graph()
    C = []
    print(graph)
    # Loop to iterate over every node
    while len(list(graph.edges)) > 0:
        choice = random.choice(list(graph.edges))
        C.append(choice[0])
        C.append(choice[1])
        graph.remove_nodes_from([choice[0],choice[1]])
    return C

print(vertex_cover())
    