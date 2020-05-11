// https://tinyurl.com/y7u3q9e7
const foldl = op => init => xs => is_null(xs) ? init : foldl(op)(op(init, head(xs)))(tail(xs));
const reverse = (xs) => foldl((out,x) => pair(x, out))(null)(xs);
reverse([2, [3, [4, [4, null]]]]);