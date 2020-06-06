// Author: Shreyas Padhye, spadhye@scu.edu, 00001556287

const KI = a => b => b;

const stream_tail = xs => tail(xs)();
const take = n => s => is_null(s) || n <= 0 ? null : 
                                              pair(head(s), () => take(n-1)(stream_tail(s)));
                                              
const take_sum = n => s => sum => is_null(s) || n <= 0 ? null : 
                                              pair(sum+head(s), () => take_sum(n-1)(stream_tail(s))(sum+head(s)));

const foreach = f => xs => is_null(xs) ? true : KI(f(head(xs)))(foreach(f)(stream_tail(xs)));
const sum_each = xs => sum => is_null(xs) ? sum : sum_each(stream_tail(xs))(sum+head(xs));
const display_stream = foreach(display);

const filter = p => s => is_null(s) ? null :
      p(head(s)) ? pair(head(s), () => filter(p)(stream_tail(s))) :
                                       filter(p)(stream_tail(s));


const fibgen = (a,b) => pair(a, () => fibgen(b, a+b));
const fibs = fibgen(0, 1);
// display_stream(take(18)(fibs));
// display("--------------");

const is_even = a => a%2 === 0;
function sieve(stream) {
  const h = head(stream);
  return pair(h, () => sieve(filter(is_even)(stream_tail(stream))));
}
const even_fibs = sieve(fibs);

even_fibs;
// display_stream(take(8)(even_fibs));
sum_each(take(100)(even_fibs))(0);
// take_sum(1000)(even_fibs)(0);
