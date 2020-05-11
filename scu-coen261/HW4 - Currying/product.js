// https://tinyurl.com/yakjfyvx
const foldr = op => init => xs => is_null(xs) ? init : op(head(xs), foldr(op)(init)(tail(xs)));
const product = (xs) => foldr((xs,n) => n*xs)(1)(xs); 
product([2, [3, [4, [4, null]]]]);