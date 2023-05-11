Because operations on matrices lie at the heart of scientific computing, efficient algorithms for working with matrices have many practical applications. This chapter
focuses on how to multiply matrices and solve sets of simultaneous linear equations. Appendix D reviews the basics of matrices.
Section 28.1 shows how to solve a set of linear equations using LUP decompositions. 

Then, Section 28.2 explores the close relationship between multiplying and
inverting matrices. Finally, Section 28.3 discusses the important class of symmetric
positive-definite matrices and shows how we can use them to find a least-squares
solution to an overdetermined set of linear equations.
One important issue that arises in practice is numerical stability. Due to the
limited precision of floating-point representations in actual computers, round-off
errors in numerical computations may become amplified over the course of a computation, leading to incorrect results; we call such computations numerically unstable. 

Although we shall briefly consider numerical stability on occasion, we do
not focus on it in this chapter. We refer you to the excellent book by Golub and
Van Loan [144] for a thorough discussion of stability issues