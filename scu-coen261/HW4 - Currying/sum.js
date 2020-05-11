// https://tinyurl.com/yahqyvxb
const foldr = op => init => xs => is_null(xs) ? init : op(head(xs), foldr(op)(init)(tail(xs)));
const sum = (xs) => foldr((xs,n) => n+xs)(0)(xs); 
sum([2, [3, [4, [4, null]]]]);