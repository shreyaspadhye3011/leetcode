// given a dictionary and a key, find a value - or return undefined
const lookup = dict => key => is_null(dict) ?  undefined :
                               head(head(dict)) === key ? tail(head(dict)) :
                               lookup(tail(dict))(key);

// given a sequence of keys and values (alternating), build a dictionary (aka table)
const table = kvpairs => is_null(kvpairs) ? null :
              pair(pair(head(kvpairs), head(tail(kvpairs))), table(tail(tail(kvpairs))));

// given a list (command1, operation1, command2, operation2, etc), build a dispatch
const dispatch = list => lookup(table(list));


// deep flattening of a list
const flatten = xs => is_null(xs) ? null : !is_list(xs) ? list(xs) :
               append(is_list(head(xs)) ? flatten(head(xs)) : list(head(xs)),
                      flatten(tail(xs)));

const flatmap = f => list => flatten(map(f)(list));

// Scan LTR
const scan = v => (!is_function(v) || (v(scan) === undefined)) ? flatten(v) : v(scan);

const single = a => dispatch(list(scan, scan(a)));    
const empty = dispatch(list(scan, null));

const tree = (left, subtree, right) => dispatch(list(
   scan, flatmap(scan)(list(left, subtree, right))));

const digit1 = a => dispatch(list(
   scan, flatmap(scan)(list(a))));
const digit2 = (a,b) => dispatch(list(
   scan, flatmap(scan)(list(a,b))));
const digit3 = (a,b,c) => dispatch(list(
   scan, flatmap(scan)(list(a,b,c))));
const digit4 = (a,b,c,d) => dispatch(list(
   scan, flatmap(scan)(list(a,b,c,d))));
const node2 = (a,b) => dispatch(list(
   scan, flatmap(scan)(list(a,b))));
const node3 = (a,b,c) => dispatch(list(
   scan, flatmap(scan)(list(a,b,c))));
