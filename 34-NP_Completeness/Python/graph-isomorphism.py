# Check if two graphs are isomorphic

import networkx as nx

def is_isomorphic(graph1, graph2):
	# Check if the number of nodes and edges are equal
	if graph1.number_of_nodes() != graph2.number_of_nodes() or graph1.number_of_edges() != graph2.number_of_edges():
		return False

	# Check if the graphs are connected
	if not nx.is_connected(graph1) or not nx.is_connected(graph2):
		return False

	# Check if the degree sequences are equal
	if sorted(nx.degree(graph1)) != sorted(nx.degree(graph2)):
		return False

	# Check if the graph structures are isomorphic using the isomorphism function from networkx
	return nx.isomorphism.isomorph.isomorph(graph1, graph2)

# Create two graphs
graph1 = nx.Graph()
graph2 = nx.Graph()
graph1.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])
graph2.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])
print(is_isomorphic(graph1, graph2))