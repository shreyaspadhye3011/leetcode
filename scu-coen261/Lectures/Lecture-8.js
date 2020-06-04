// Generate fibonacci numbers using stream
const KI = a => b => b;
const stream_tail = xs => tail(xs)();
const take = n => s => is_null(s) || n <= 0 ? null : 
                                              pair(head(s), () => take(n-1)(stream_tail(s)));

const foreach = f => xs => is_null(xs) ? true : KI(f(head(xs)))(foreach(f)(stream_tail(xs)));
const display_stream = foreach(display);
const fibgen = (a,b) => pair(a, () => fibgen(b, a+b));
const fibs = fibgen(0, 1);
display_stream(take(8)(fibs));