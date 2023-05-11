The vast majority of algorithms in this book are serial algorithms suitable for
running on a uniprocessor computer in which only one instruction executes at a
time. In this chapter, we shall extend our algorithmic model to encompass parallel
algorithms, which can run on a multiprocessor computer that permits multiple
instructions to execute concurrently. In particular, we shall explore the elegant
model of dynamic multithreaded algorithms, which are amenable to algorithmic
design and analysis, as well as to efficient implementation in practice.
Parallel computers—computers with multiple processing units—have become
increasingly common, and they span a wide range of prices and performance. Relatively inexpensive desktop and laptop chip multiprocessors contain a single multicore integrated-circuit chip that houses multiple processing “cores,” each of which
is a full-fledged processor that can access a common memory. At an intermediate price/performance point are clusters built from individual computers—often
simple PC-class machines—with a dedicated network interconnecting them.

The
highest-priced machines are supercomputers, which often use a combination of
custom architectures and custom networks to deliver the highest performance in
terms of instructions executed per second.
Multiprocessor computers have been around, in one form or another, for
decades. Although the computing community settled on the random-access machine model for serial computing early on in the history of computer science, no
single model for parallel computing has gained as wide acceptance. A major reason is that vendors have not agreed on a single architectural model for parallel
computers. 

For example, some parallel computers feature shared memory, where
each processor can directly access any location of memory. Other parallel computers employ distributed memory, where each processor’s memory is private, and
an explicit message must be sent between processors in order for one processor to
access the memory of another. With the advent of multicore technology, however,
every new laptop and desktop machine is now a shared-memory parallel computer, and the trend appears to be toward shared-memory multiprocessing. Although time
will tell, that is the approach we shall take in this chapter.
One common means of programming chip multiprocessors and other sharedmemory parallel computers is by using static threading, which provides a software
abstraction of “virtual processors,” or threads, sharing a common memory. Each
thread maintains an associated program counter and can execute code independently of the other threads. The operating system loads a thread onto a processor
for execution and switches it out when another thread needs to run. Although the
operating system allows programmers to create and destroy threads, these operations are comparatively slow. Thus, for most applications, threads persist for the
duration of a computation, which is why we call them “static.”


Unfortunately, programming a shared-memory parallel computer directly using
static threads is difficult and error-prone. One reason is that dynamically partitioning the work among the threads so that each thread receives approximately
the same load turns out to be a complicated undertaking. For any but the simplest of applications, the programmer must use complex communication protocols
to implement a scheduler to load-balance the work. This state of affairs has led
toward the creation of concurrency platforms, which provide a layer of software
that coordinates, schedules, and manages the parallel-computing resources. Some
concurrency platforms are built as runtime libraries, but others provide full-fledged
parallel languages with compiler and runtime support.
