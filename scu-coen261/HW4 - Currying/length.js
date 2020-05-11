// https://tinyurl.com/y8au9jum
const foldr = op => init => xs => is_null(xs) ? init : op(head(xs), foldr(op)(init)(tail(xs)));
const length = (xs) => foldr((xs,n) => n+1)(0)(xs); 
length([2, [3, [4, [4, null]]]]);