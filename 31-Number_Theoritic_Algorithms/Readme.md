Number theory was once viewed as a beautiful but largely useless subject in pure
mathematics. Today number-theoretic algorithms are used widely, due in large part
to the invention of cryptographic schemes based on large prime numbers. These
schemes are feasible because we can find large primes easily, and they are secure
because we do not know how to factor the product of large primes (or solve related
problems, such as computing discrete logarithms) efficiently. This chapter presents
some of the number theory and related algorithms that underlie such applications.


Section 31.1 introduces basic concepts of number theory, such as divisibility,
modular equivalence, and unique factorization. Section 31.2 studies one of the
world’s oldest algorithms: Euclid’s algorithm for computing the greatest common
divisor of two integers. Section 31.3 reviews concepts of modular arithmetic. 

Section 31.4 then studies the set of multiples of a given number a, modulo n, and shows
how to find all solutions to the equation $ax \equiv b \mod n$ by using Euclid’s algorithm. The Chinese remainder theorem is presented in Section 31.5. Section 31.6
considers powers of a given number a, modulo n, and presents a repeated-squaring
algorithm for efficiently computing ab mod n, given a, b, and n. This operation is
at the heart of efficient primality testing and of much modern cryptography. 

Section 31.7 then describes the RSA public-key cryptosystem. Section 31.8 examines
a randomized primality test. We can use this test to find large primes efficiently,
which we need to do in order to create keys for the RSA cryptosystem. Finally,
Section 31.9 reviews a simple but effective heuristic for factoring small integers. It
is a curious fact that factoring is one problem people may wish to be intractable,
since the security of RSA depends on the difficulty of factoring large integers.