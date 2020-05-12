// https://tinyurl.com/ydg57gjk

const foldr = op => init => xs => is_null(xs) ? init : op(head(xs), foldr(op)(init)(tail(xs)));
const foldl = op => init => xs => is_null(xs) ? init : foldl(op)(op(init, head(xs)))(tail(xs));

// Basics
const Nil = null;
const Cons = a => remaining => append(list(a), remaining);
const Const = a => b => a;
const flip = xs => list(tail(xs), head(xs));

// 1. length
const length = (xs) => foldr((xs,n) => n+1)(0)(xs); 
display(length([2, [3, [4, [4, null]]]]), "Length:");

// 2. sum
const sum = (xs) => foldr((xs,n) => n+xs)(0)(xs); 
display(sum([2, [3, [4, [4, null]]]]), "Sum:");

// 3. product
const product = (xs) => foldr((xs,n) => n*xs)(1)(xs); 
display(product([2, [3, [4, [4, null]]]]), "Product:");

// 4. map
const map = (f) => (xs) => is_null(xs) ? null : pair(f(head(xs)), map(f)(tail(xs)));
display(map(x => x *2)([2, [3, [4, [4, null]]]]), "Map to double:");

// 5. reverse
const reverse = (xs) => foldl((out,x) => pair(x, out))(null)(xs);
display(reverse([2, [3, [4, [4, null]]]]), "Reversed List:");

// 6. flatten
const flatten = (xs) => foldr((xs, ys) => append(xs, ys))(null)(xs);
display(flatten([[2, null], [[3, [7, null]], [[4, [8, [3, null]]], [[4, null], null]]]]), "Flatten result:");

// 7. heador
const heador = xs => default_value => is_null(xs) ? default_value : head(xs); 
display(heador([2, [3, [4, [4, null]]]])(-1), "Heador:");
display(heador(null)(-1), "Heador (default):");


