#include <bits/stdc++.h>
using namespace std;

class Graph
{
    int V;
    list<int> *adj;

public:
    Graph(int V);
    void addEdge(int u, int v);
    bool isReachable(int s, int d, int k);
};

Graph::Graph(int V)
{
    this->V = V;
    adj = new list<int>[V];
}

void Graph::addEdge(int u, int v)
{
    adj[u].push_back(v);
}

bool Graph::isReachable(int s, int d, int k)
{
    if (k == 0 && s != d)
        return false;

    if (k == 1 && adj[s].find(d) != adj[s].end())
        return true;

    list<int>::iterator i;
    for (i = adj[s].begin(); i != adj[s].end(); ++i)
        if (isReachable(*i, d, k - 1) == true)
            return true;

    return false;
}

int main()
{
    int V = 9;
    Graph g(V);

    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(0, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 5);
    g.addEdge(2, 6);
    g.addEdge(3, 7);
    g.addEdge(4, 8);
    g.addEdge(5, 8);
    g.addEdge(6, 8);
    g.addEdge(7, 8);

    int u = 0, v = 8, k = 4;
    if (g.isReachable(u, v, k))
        cout << "Yes";
    else
        cout << "No";

    return 0;
}