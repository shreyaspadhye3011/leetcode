// Author: Shreyas Padhye, spadhye@scu.edu, 00001556287
// Courtesy: Prof. Vlad Patryshev & SICP JS

// stream basics
const KI = a => b => b;

const stream_tail = xs => tail(xs)();
const take = n => s => is_null(s) || n <= 0 ? null : 
                                              pair(head(s), () => take(n-1)(stream_tail(s)));

const foreach = f => xs => is_null(xs) ? "." : KI(f(head(xs)))(foreach(f)(stream_tail(xs)));
const display_stream = foreach(display);

// stream generator for double factorial based on https://mathworld.wolfram.com/DoubleFactorial.html 
const double_factorial_gen = n => (n === 0 || n === -1) ? pair(1, null) : pair(n * head(double_factorial_gen(n-2)), () => double_factorial_gen(n+1));
const double_factorial = double_factorial_gen(1);

display_stream(take(8)(double_factorial));