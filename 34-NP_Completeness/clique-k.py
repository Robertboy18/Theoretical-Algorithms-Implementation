import networkx as nx
import itertools

def find_clique(G,k):
    for subset in itertools.combinations(G.nodes(), k):
        if nx.is_clique(G, subset):
            return subset
    return None

G = nx.Graph()
G.add_edges_from([(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8)])
k = 2
print(find_clique(G,k))