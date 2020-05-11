// https://tinyurl.com/y825fc8e
const map = (f) => (xs) => is_null(xs) ? null : pair(f(head(xs)), map(f)(tail(xs)));
map(x => x *2)([2, [3, [4, [4, null]]]]);