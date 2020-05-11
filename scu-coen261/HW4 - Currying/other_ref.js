const Nil = null;
const Cons = a => restOfList => append(list(a), restOfList);
const Const = x => y => x;
const flip = l => list(tail(l), head(l));

const foldr = op => init => values => length(values) === 0 ? init : op(head(values))(foldr(op)(init)(tail(values)));
const foldl = op => init => values => length(values) === 0 ? init : foldl(op)(op(init)(head(values)))(tail(values));

// Here are the values used for testing my functions:
const myList = Cons(1)(Cons(2)(Cons(3)(Cons(4)(Nil))));
const myListOfLists = Cons(Cons(10)(Nil))(Cons(20)(Nil));
const myDefaultValue = 100;

const lengthList = l => foldl(a => b => a + 1)(0)(l);
display(lengthList(myList));

const sum = l => foldl(a => b => (a + b))(0)(l);
display(sum(myList));

const product = l => foldl(a => b => (a * b))(1)(l);
display(product(myList));

const map = f => l => foldr(a => b => Cons(f(a))(b))(Nil)(l);
display(map(a => a + 10)(myList));

const reverse = l => foldl(a => b => Cons(b)(a))(Nil)(l);
display(reverse(myList));

const flatten = l => foldr(Cons)(Nil)(l);
display(flatten(myListOfLists));

const heador = value => l => foldr(Const)(value)(l);
display(heador(myDefaultValue)(myList));
display(heador(myDefaultValue)(Nil));