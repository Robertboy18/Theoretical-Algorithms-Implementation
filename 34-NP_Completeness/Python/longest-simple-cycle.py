import sys
import networkx as nx

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 longest_simple_cycle.py <graph_file>")
        sys.exit(1)

    graph_file = sys.argv[1]
    G = nx.read_edgelist(graph_file, create_using=nx.DiGraph())

    # Find the longest simple cycle in the graph
    cycle = nx.simple_cycles(G)
    longest_cycle = max(cycle, key=len)

    # Print the longest simple cycle
    print("Longest simple cycle:")
    print(longest_cycle)

if __name__ == "__main__":
    main()