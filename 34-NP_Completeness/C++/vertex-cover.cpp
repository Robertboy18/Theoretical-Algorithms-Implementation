#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define V 5

void printSolution(int cover[])
{
    printf("Vertex cover is: ");
    for (int i = 0; i < V; i)
        if (cover[i])
            printf("%d ", i);
    printf("\n");
}

bool isSafe(bool graph[V][V], int cover[], int i)
{
    for (int j = 0; j < V; j)
        if (graph[i][j] && cover[j])
            return false;
    return true;
}

bool vertexCover(bool graph[V][V], int cover[], int i)
{
    if (i == V)
        return true;

    if (isSafe(graph, cover, i))
    {
        cover[i] = 1;
        if (vertexCover(graph, cover, i  1))
            return true;
        cover[i] = 0;
    }

    if (vertexCover(graph, cover, i  1))
        return true;

    return false;
}

bool isVertexCover(bool graph[V][V], int k)
{
    int cover[V];
    for (int i = 0; i < V; i)
        cover[i] = 0;

    if (!vertexCover(graph, cover, 0))
        return false;

    int count = 0;
    for (int i = 0; i < V; i)
        if (cover[i])
            count;

    if (count <= k)
    {
        printSolution(cover);
        return true;
    }
    else
        return false;
}

int main()
{
    bool graph[V][V] = {
        {0, 1, 1, 1, 0},
        {1, 0, 0, 0, 1},
        {1, 0, 0, 0, 1},
        {1, 0, 0, 0, 1},
        {0, 1, 1, 1, 0},
    };
    int k = 2;
    if (!isVertexCover(graph, k))
        printf("No vertex cover of size %d exists\n", k);
    return 0;
}