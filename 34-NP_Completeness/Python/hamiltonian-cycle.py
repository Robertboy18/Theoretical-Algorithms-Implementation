import itertools

def find_hamiltonian_cycle(graph, vertex_count):
	# Create a list of all possible vertex permutations
	vertex_permutations = list(itertools.permutations(range(vertex_count)))

	# Iterate through each permutation
	for permutation in vertex_permutations:
		# Check if the permutation is a valid Hamiltonian cycle
		is_valid = True
		for i in range(vertex_count - 1):
			if not graph[permutation[i]][permutation[i+1]]:
				is_valid = False
				break
		if is_valid and graph[permutation[-1]][permutation[0]]:
			return permutation

	# If no valid Hamiltonian cycle was found, return None
	return None