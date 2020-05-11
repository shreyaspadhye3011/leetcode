// https://tinyurl.com/yajftnt3
const foldr = op => init => xs => is_null(xs) ? init : op(head(xs), foldr(op)(init)(tail(xs)));
const flatten = (xs) => foldr((xs, ys) => append(xs, ys))(null)(xs);
flatten([[2, null], [[3, [7, null]], [[4, [8, [3, null]]], [[4, null], null]]]]);