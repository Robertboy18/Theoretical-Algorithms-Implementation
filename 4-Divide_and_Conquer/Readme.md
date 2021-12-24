Recall that in divide-and-conquer, we solve a problem recursively, applying three steps at each level of the recursion:
Divide the problem into a number of subproblems that are smaller instances of the
same problem.
Conquer the subproblems by solving them recursively. If the subproblem sizes are
small enough, however, just solve the subproblems in a straightforward manner.
Combine the solutions to the subproblems into the solution for the original problem.
When the subproblems are large enough to solve recursively, we call that the recursive case. Once the subproblems become small enough that we no longer recurse,
we say that the recursion “bottoms out” and that we have gotten down to the base
case. Sometimes, in addition to subproblems that are smaller instances of the same
problem, we have to solve subproblems that are not quite the same as the original
problem. We consider solving such subproblems as part of the combine step.
