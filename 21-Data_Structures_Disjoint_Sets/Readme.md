Some applications involve grouping n distinct elements into a collection of disjoint
sets. These applications often need to perform two operations in particular: finding
the unique set that contains a given element and uniting two sets. This chapter
explores methods for maintaining a data structure that supports these operations.
Section 21.1 describes the operations supported by a disjoint-set data structure
and presents a simple application. In Section 21.2, we look at a simple linked-list
implementation for disjoint sets. Section 21.3 presents a more efficient representation using rooted trees. The running time using the tree representation is theoretically superlinear, but for all practical purposes it is linear. Section 21.4 defines
and discusses a very quickly growing function and its very slowly growing inverse,
which appears in the running time of operations on the tree-based implementation,
and then, by a complex amortized analysis, proves an upper bound on the running
time that is just barely superlinear