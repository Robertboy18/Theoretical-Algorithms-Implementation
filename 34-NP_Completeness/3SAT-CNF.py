import itertools

def is_satisfiable(clauses):
	# Get all possible assignments for the variables
	assignments = list(itertools.product([True, False], repeat=len(variables)))

	# Check if any of the assignments satisfies all clauses
	for assignment in assignments:
		satisfied = True
		for clause in clauses:
			clause_satisfied = False
			for literal in clause:
				if literal > 0:
					if assignment[literal-1] == True:
						clause_satisfied = True
						break
				else:
					if assignment[abs(literal)-1] == False:
						clause_satisfied = True
						break
			if not clause_satisfied:
				satisfied = False
				break
		if satisfied:
			return True

	return False

# Test the function
clauses = [[1, 2, 3], [-1, 2, 3], [1, -2, 3], [1, 2, -3], [-1, -2, 3], [-1, 2, -3], [1, -2, -3], [-1, -2, -3]]
print(is_satisfiable(clauses))