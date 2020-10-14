# Master Theorem
Let a ≥ 1 and b > 1 be constants, let f(n) be a function, and let T(n) be a function over the positive numbers defined by the recurrence

T(n) = aT(n/b) + f(n).
If f(n) = Θ(n^d), where d ≥ 0, then

T(n) = Θ(n^d) if a < b^d,
T(n) = Θ(n^d log n) if a = b^d,
T(n) = Θ(n^log (base)b a) if a > b^d.

NOTICE: b > 1. It can't be 1. i.e Master theorem is used for solving divide and conquer type problems where problem size is reducing exponentially.

For other problems, use substitution. -- Mostly Factorial

# Todo: add examples. add factorial solution

# Loops
for (i=a; i <= b; i++)      // (b-a+1)
for (i=a; i <= b; i+=2)     // O(b-a+1) - when inc or dec by a constant amount
for (i=a; i <= b; i*=2)     // log(b-a+1) - when multiplied or divided by a constant amount

# Dynamic Arrays: amortized analysis
TL;DR:
1. Insertion at end: Amortized O(1)
2. Insertion at middle or end: O(N)

Reference: AlgoExpert
1. Lists in Python or arrays in JavsScript are dynamic arrays underhood
2. For static arrays, increasing array size, inserting in  middle or end or front is O(N) time & O(1) space: Process: copy the whole array to a new location which can hold the updated size of the array. Array is always contiguous memory blocks. O(1) space because the old space is cleared once copied
3. To solve, this we use dynamic array which does two things:
    a. Allocate 2 * N size during init
    b. While appending (in the end), if you run out of space, always add 2 * N new blocks (by same copy method as static array). Therefore, whenever you run out of space, you give yourself double the space. Thus, giving constant time insertions for a long time as space is available and no copy / shift is required
    
    This leads to an amortized complexity of O(1) for append in dynamic arrays. Notice that the worst case when you run out of memory is taking O(N) time but OVERALL the constant time insertions dominate. Therefore, O(1)
4. Note that insertion at front or middle is still O(N) in case of dynamic array. though the extra double init space does help but you need to always perform SHIFT operation for insertion in front or middle

