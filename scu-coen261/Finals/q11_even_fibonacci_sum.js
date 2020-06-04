// Author: Shreyas Padhye, spadhye@scu.edu, 00001556287

const KI = a => b => b;

const stream_tail = xs => tail(xs)();
const take = n => s => is_null(s) || n <= 0 ? null : 
                                              pair(head(s), () => take(n-1)(stream_tail(s)));

const foreach = f => xs => is_null(xs) ? true : KI(f(head(xs)))(foreach(f)(stream_tail(xs)));
const display_stream = foreach(display);

const filter = p => s => is_null(s) ? null :
      p(head(s)) ? pair(head(s), () => filter(p)(stream_tail(s))) :
                                       filter(p)(stream_tail(s));


const fibgen = (a,b) => pair(a, () => fibgen(b, a+b));
const fibs = fibgen(0, 1);
display_stream(take(18)(fibs));

display("--------------");

const is_even = a => a%2 === 0;
function sieve(stream) {
  const h = head(stream);
  return pair(h, () => sieve(filter(is_even)(stream_tail(stream))));
}
const even_fibs = sieve(fibs);

even_fibs;
display_stream(take(8)(even_fibs));
