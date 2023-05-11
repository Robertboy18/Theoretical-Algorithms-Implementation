Professor Patrick wishes to find the shortest possible route from Phoenix to Indianapolis. Given a road map of the United States on which the distance between each pair of adjacent intersections is marked, how can she determine this shortest route?

One possible way would be to enumerate all the routes from Phoenix to Indianapolis, add up the distances on each route, and select the shortest. It is easy to see, however, that even disallowing routes that contain cycles, Professor Patrick would have to examine an enormous number of possibilities, most of which are simply not worth considering. For example, a route from Phoenix to Indianapolis that passes through Seattle is obviously a poor choice, because Seattle is several hundred miles out of the way.

In this chapter and in Chapter 25, we show how to solve such problems efficiently. In a shortest-paths problem, we are given a weighted, directed graph $G=(V, E)$, with weight function $w: E \rightarrow \mathbb{R}$ mapping edges to real-valued weights. The weight $w(p)$ of path $p=\left\langle v_0, v_1, \ldots, v_k\right\rangle$ is the sum of the weights of its constituent edges:
$$
w(p)=\sum_{i=1}^k w\left(v_{i-1}, v_i\right)
$$
We define the shortest-path weight $\delta(u, v)$ from $u$ to $v$ by
$$
\delta(u, v)= \begin{cases}\min \{w(p): u \stackrel{p}{\rightarrow} v\} & \text { if there is a path from } u \text { to } v, \\ \infty & \text { otherwise. }\end{cases}
$$
A shortest path from vertex $u$ to vertex $v$ is then defined as any path $p$ with weight $w(p)=\delta(u, v)$

In the Phoenix-to-Indianapolis example, we can model the road map as a graph: vertices represent intersections, edges represent road segments between intersections, and edge weights represent road distances. Our goal is to find a shortest path from a given intersection in Phoenix to a given intersection in Indianapolis. 

Edge weights can represent metrics other than distances, such as time, cost, penalties, loss, or any other quantity that accumulates linearly along a path and that we would want to minimize.

The breadth-first-search algorithm from Section 22.2 is a shortest-paths algorithm that works on unweighted graphs, that is, graphs in which each edge has unit weight. Because many of the concepts from breadth-first search arise in the study of shortest paths in weighted graphs, you might want to review Section 22.2 before proceeding.
Variants
In this chapter, we shall focus on the single-source shortest-paths problem: given a graph $G=(V, E)$, we want to find a shortest path from a given source vertex $s \in V$ to each vertex $v \in V$. The algorithm for the single-source problem can solve many other problems, including the following variants.

Single-destination shortest-paths problem: Find a shortest path to a given destination vertex $t$ from each vertex $v$. By reversing the direction of each edge in the graph, we can reduce this problem to a single-source problem.

Single-pair shortest-path problem: Find a shortest path from $u$ to $v$ for given vertices $u$ and $v$. If we solve the single-source problem with source vertex $u$, we solve this problem also. Moreover, all known algorithms for this problem have the same worst-case asymptotic running time as the best single-source algorithms.

All-pairs shortest-paths problem: Find a shortest path from $u$ to $v$ for every pair of vertices $u$ and $v$. Although we can solve this problem by running a singlesource algorithm once from each vertex, we usually can solve it faster. Additionally, its structure is interesting in its own right. Chapter 25 addresses the all-pairs problem in detail.