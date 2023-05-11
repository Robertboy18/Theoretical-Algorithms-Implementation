Many problems of practical significance are NP-complete, yet they are too important to abandon merely because we don’t know how to find an optimal solution in
polynomial time. Even if a problem is NP-complete, there may be hope. We have at
least three ways to get around NP-completeness. First, if the actual inputs are small,
an algorithm with exponential running time may be perfectly satisfactory. Second,
we may be able to isolate important special cases that we can solve in polynomial
time. Third, we might come up with approaches to find near-optimal solutions in
polynomial time (either in the worst case or the expected case). In practice, near optimality is often good enough. We call an algorithm that returns near-optimal
solutions an approximation algorithm. This chapter presents polynomial-time approximation algorithms for several NP-complete problems