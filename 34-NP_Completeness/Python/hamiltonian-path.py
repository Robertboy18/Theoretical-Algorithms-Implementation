import networkx as nx

def has_hamiltonian_path(graph):
# Check if the graph is a directed graph
	if not graph.is_directed():
		return False

	# Check if the graph is connected
	if not nx.is_weakly_connected(graph):
		return False

	# Check if the graph has a cycle
	if not nx.is_directed_acyclic_graph(graph):
		return False

	# Check if the graph has at least as many vertices as the longest possible Hamiltonian path
	if len(graph) < nx.dag_longest_path_length(graph):
		return False

	return True