# Circuit Satisfiability

def is_satisfiable(circuit):
# Initialize a stack to store the variables
	stack = []

	# Iterate through the circuit
	for clause in circuit:
		# If the clause is a variable, push it onto the stack
		if isinstance(clause, int):
			stack.append(clause)
		# If the clause is a negation, negate the top variable on the stack
		elif clause == "NOT":
			top = stack.pop()
			stack.append(-top)
		# If the clause is an OR, pop the top two variables and OR them together
		elif clause == "OR":
			top1 = stack.pop()
			top2 = stack.pop()
			stack.append(top1 or top2)
		# If the clause is an AND, pop the top two variables and AND them together
		elif clause == "AND":
			top1 = stack.pop()
			top2 = stack.pop()
			stack.append(top1 and top2)

	# If the stack is empty or the top variable is false, the circuit is not satisfiable
	if not stack or not stack[-1]:
		return False
	# Otherwise, the circuit is satisfiable
	else:
		return True
	
# Test the function
circuit = [1, "NOT", "OR", 2, "AND", 3, "OR"]
print(is_satisfiable(circuit))