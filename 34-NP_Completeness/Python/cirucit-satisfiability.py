import random
import sys

def try_all_values(N, clauses, model):
    if len(clauses) == 0:
        print(model)
        exit(0)
    else:
        P, value = clauses[0]
        rest = clauses[1:]
        model_copy = model.copy()
        model_copy[P] = value
        try_all_values(N, rest, model_copy)
        model_copy[P] = 1 - value
        try_all_values(N, rest, model_copy)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 sat.py <filename>")
        exit(1)
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        N = int(f.readline())
        clauses = []
        for line in f:
            clause = []
            for literal in line.split():
                P = int(literal)
                if P == 0:
                    break
                clause.append(P)
            clauses.append(clause)
    model = {}
    for i in range(1, N+1):
        model[i] = random.randint(0, 1)
    try_all_values(N, clauses, model)

if __name__ == '__main__':
    main()