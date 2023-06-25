# Author: Robert Joseph

import unittest

# Function to check if the given assignment satisfies the 3-SAT formula
def checkSatisfiability(formula, assignment):
    """
    Checks if the given assignment satisfies the 3-SAT formula.
    :param formula: The 3-SAT formula as a list of tuples.
    :param assignment: The assignment of variables as a dictionary.
    :return: True if the assignment satisfies the formula, False otherwise.
    """
    # Loop through all the clauses in the formula
    for clause in formula:
        # If the clause is satisfied by the given assignment, continue to the next clause
        if (assignment[clause[0]] and clause[1] == 1) or (not assignment[clause[0]] and clause[1] == 0) or \
           (assignment[clause[2]] and clause[3] == 1) or (not assignment[clause[2]] and clause[3] == 0) or \
           (assignment[clause[4]] and clause[5] == 1) or (not assignment[clause[4]] and clause[5] == 0):
            continue
        # If the clause is not satisfied, return False
        else:
            return False
    # If all the clauses are satisfied, return True
    return True

# Function to solve the 3-SAT problem using the DPLL algorithm
def dpll(formula):
    """
    Solves the 3-SAT problem using the DPLL algorithm.
    :param formula: The 3-SAT formula as a list of tuples.
    :return: True if the formula is satisfiable, False otherwise.
    """
    # Set of all the variables in the formula
    variables = set()
    # Loop through all the clauses in the formula
    for clause in formula:
        # Add all the variables in the clause to the set of variables
        variables.add(clause[0])
        variables.add(clause[2])
        variables.add(clause[4])

    # Dictionary to store the current assignment of variables
    assignment = {}
    # Initialize all the variables with False
    for variable in variables:
        assignment[variable] = False

    # Call the recursive function to solve the 3-SAT problem
    return dpllRecursive(formula, variables, assignment)

# Function to solve the 3-SAT problem recursively using the DPLL algorithm
def dpllRecursive(formula, variables, assignment):
    """
    Solves the 3-SAT problem recursively using the DPLL algorithm.
    :param formula: The 3-SAT formula as a list of tuples.
    :param variables: The set of variables.
    :param assignment: The current assignment of variables.
    :return: True if the formula is satisfiable, False otherwise.
    """
    # If all the variables have been assigned a value, check if the formula is satisfied
    if not variables:
        return checkSatisfiability(formula, assignment)

    # Select the first variable from the set of variables
    variable = variables.pop()

    # Create a copy of the current assignment
    assignment1 = assignment.copy()
    # Assign the first variable True and recursively solve the 3-SAT problem
    assignment1[variable] = True
    result1 = dpllRecursive(formula, variables, assignment1)
    # If the result is True, return True
    if result1:
        return True

    # Create a copy of the current assignment
    assignment2 = assignment.copy()
    # Assign the first variable False and recursively solve the 3-SAT problem
    assignment2[variable] = False
    result2 = dpllRecursive(formula, variables, assignment2)
    # If the result is True, return True
    if result2:
        return True

    # If both the assignments did not result in True, return False
    return False


class TestDPLL(unittest.TestCase):
    def test_dpll(self):
        # Test case 1: Unsatisfiable formula
        formula = [
            (1, 1, 2, 0, 3, 1),  # (x1 OR ~x2 OR x3)
            (1, 0, 2, 1, 3, 0),  # (x1 OR x2 OR ~x3)
            (1, 1, 2, 0, 3, 0)   # (x1 OR ~x2 OR ~x3)
        ]
        self.assertFalse(dpll(formula))

        # Test case 2: Satisfiable formula
        formula = [
            (1, 0, 2, 0, 3, 1),  # (~x1 OR ~x2 OR x3)
            (1, 1, 2, 1, 3, 0),  # (x1 OR x2 OR ~x3)
            (1, 0, 2, 1, 3, 0)   # (~x1 OR x2 OR ~x3)
        ]
        self.assertTrue(dpll(formula))

        # Test case 3: Satisfiable formula
        formula = [
            (1, 1, 2, 1, 3, 1),  # (x1 OR x2 OR x3)
            (1, 0, 2, 0, 3, 1),  # (~x1 OR ~x2 OR x3)
            (1, 0, 2, 1, 3, 1)   # (~x1 OR x2 OR x3)
        ]
        self.assertTrue(dpll(formula))


if __name__ == '__main__':
    unittest.main()
