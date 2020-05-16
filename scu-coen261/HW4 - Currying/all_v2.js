// https://tinyurl.com/y9lvbehp

const foldr = op => init => xs => is_null(xs) ? init : op(head(xs), foldr(op)(init)(tail(xs)));
const foldl = op => init => xs => is_null(xs) ? init : foldl(op)(op(init, head(xs)))(tail(xs));

// Basics
const Nil = null;
const Cons = a => remaining => append(list(a), remaining);
const Const = a => b => a;
const flip = xs => list(tail(xs), head(xs));

// 1. length
const length = (xs) => foldr((xs,n) => n+1)(0)(xs); 
display(length(Cons(2)(Cons(3)(Cons(4)(Cons(4)(Nil))))), "Length:");

// 2. sum
const sum = (xs) => foldr((xs,n) => n+xs)(0)(xs); 
display(sum(Cons(2)(Cons(3)(Cons(4)(Cons(4)(Nil))))), "Sum:");

// 3. product
const product = (xs) => foldr((xs,n) => n*xs)(1)(xs); 
display(product(Cons(2)(Cons(3)(Cons(4)(Cons(4)(Nil))))), "Product:");

// 4. map
const map = (f) => (xs) => foldr((a,b) => Cons(f(a))(b))(Nil)(xs);
display(map(x => x *2)(Cons(2)(Cons(3)(Cons(4)(Cons(4)(Nil))))), "Map to double:");

// 5. reverse
const reverse = (xs) => foldl((a,b) => Cons(b)(a))(Nil)(xs);
display(reverse(Cons(2)(Cons(3)(Cons(4)(Cons(4)(Nil))))), "Reversed List:");

// 6. flatten
const flatten = (xs) => foldr((xs, ys) => append(xs, ys))(null)(xs);
display(flatten([[2, null], [[3, [7, null]], [[4, [8, [3, null]]], [[4, null], null]]]]), "Flatten result:");

// 7. heador
const heador = xs => default_value => foldr((a,b) => a)(default_value)(xs);
display(heador(Cons(2)(Cons(3)(Cons(4)(Cons(4)(Nil)))))(-1), "Heador:");
display(heador(null)(-1), "Heador (default):");
