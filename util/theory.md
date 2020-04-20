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

