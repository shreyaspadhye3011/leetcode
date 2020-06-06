// Author: Shreyas Padhye, spadhye@scu.edu, 00001556287
// Courtesy: Prof. Vlad Patryshev & SICP JS

const lookup = dict => key => is_null(dict) ?  undefined :
                              head(head(dict)) === key ? tail(head(dict)) :
                              lookup(tail(dict))(key);
const table = kvpairs => is_null(kvpairs) ? null :
              pair(pair(head(kvpairs), head(tail(kvpairs))), table(tail(tail(kvpairs))));

const flatten = xs => is_null(xs) ? null : !is_list(xs) ? list(xs) :
               append(is_list(head(xs)) ? flatten(head(xs)) : list(head(xs)),
                      flatten(tail(xs)));

const dispatch = list => lookup(table(list));
const map = f => list => is_null(list) ? null : pair(f(head(list)), map(f)(tail(list)));
const flatmap = f => list => flatten(map(f)(list));

const cons = tree => tree(cons);

const foldl = (op, z) => x => (!is_function(x) || (x(foldl) === undefined)) ? op(z,x) : x(foldl)(op,z);
const foldr = (op, z) => x => (!is_function(x) || (x(foldr) === undefined)) ? op(z,x) : x(foldr)(op,z);

const single = a => dispatch(list(
    cons, b => tree(digit1(b), empty, digit1(a)),
    foldl, (op,z) => foldl(op,z)(a),
    foldr, (op,z) => foldr(op,z)(a)
));    

const empty = dispatch(list(
    cons, single,
    foldl, (op,z) => z,
    foldr, (op,z) => z
));

const tree = (left, subtree, right) => dispatch(list(
  cons, x => left(cons)(subtree, right)(x),
  foldl, (op,z) => op(op(op(z,foldl(op,z)(left)),foldl(op,z)(subtree)),foldl(op,z)(right)),
  foldr, (op,z) => op(op(op(z,foldr(op,z)(left)),foldr(op,z)(subtree)),foldr(op,z)(right))
));

const digit1 = a => dispatch(list(
  cons, (subtree, right) => x => tree(digit2(x,a), subtree, right),
  foldl, (op,z) => foldl(op,z)(a),
  foldr, (op,z) => foldr(op,z)(a)
));

const digit2 = (a,b) => dispatch(list(
  cons, (subtree, right) => x => tree(digit3(x,a,b), subtree, right),
  foldl, (op,z) => op(foldl(op,z)(a),foldl(op,z)(b)),
  foldr, (op,z) => op(foldr(op,z)(a),foldr(op,z)(b))
));

const digit3 = (a,b,c) => dispatch(list(
  cons,(subtree, right) => x => tree(digit4(x,a,b,c), subtree, right),
  foldl, (op,z) => op(op(foldl(op,z)(a),foldl(op,z)(b)),foldl(op,z)(c)),
  foldr, (op,z) => op(op(foldr(op,z)(a),foldr(op,z)(b)),foldr(op,z)(c))
));

const digit4 = (a,b,c,d) => dispatch(list(
  cons,(subtree, right) => x => tree(digit2(x,a),subtree(cons)(node3(b,c,d)),right),
  foldl, (op,z) => op(op(op(foldl(op,z)(a),foldl(op,z)(b)),foldl(op,z)(c)),foldl(op,z)(d)),
  foldr, (op,z) => op(op(op(foldr(op,z)(a),foldr(op,z)(b)),foldr(op,z)(c)),foldr(op,z)(d))
));

const node2 = (a,b) => dispatch(list(
  foldl, (op,z) => op(op(z,foldl(op,z)(a)),foldl(op,z)(b)),
  foldr, (op,z) => op(op(z,foldr(op,z)(a)),foldr(op,z)(b))
));

const node3 = (a,b,c) => dispatch(list(
  foldl, (op,z) => op(op(op(z,foldl(op,z)(a)),foldl(op,z)(b)),foldl(op,z)(c)),
  foldr, (op,z) => op(op(op(z,foldr(op,z)(a)),foldr(op,z)(b)),foldr(op,z)(c))
));

const build = n => n === 0 ? empty : build(n-1)(cons)(n);
const t = build(30);
display(t(foldr)((x,y)=>x+y,0));


