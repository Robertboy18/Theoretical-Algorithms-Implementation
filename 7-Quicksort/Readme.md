The quicksort algorithm has a worst-case running time of $\Theta(n^2)$ on an input array
of n numbers. Despite this slow worst-case running time, quicksort is often the best
practical choice for sorting because it is remarkably efficient on the average: its
expected running time is $\Theta(n \log n)$, and the constant factors hidden in the ‚$\Theta(n \log n)$
notation are quite small. It also has the advantage of sorting in place 
and it works well even in virtual-memory environments.
Section 7.1 describes the algorithm and an important subroutine used by quicksort for partitioning. Because the behavior of quicksort is complex, we start with
an intuitive discussion of its performance in Section 7.2 and postpone its precise
analysis to the end of the chapter. Section 7.3 presents a version of quicksort that
uses random sampling. This algorithm has a good expected running time, and no
particular input elicits its worst-case behavior. Section 7.4 analyzes the randomized algorithm, showing that it runs in $\Theta(n^2)$ time in the worst case and, assuming
distinct elements, in expected $\operatorname{O}(n \log n)$ time.