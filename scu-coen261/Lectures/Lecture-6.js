// Tree basics
// TODO: handle null case
function top(tree) { return head(tree);}
function left(tree) { return head(tail(tree));}
function right(tree) { return head(tail(tail(tree)));} // a bit weird, right?

function tree(value, left, right) {
  return list(value, left, right);
}

const a = tree(4, list(5,7), 6);
top(a);
right(a);
left(left(a));
// right(left(a)); 

// ------------------------------------------------ //

// My PR: 
// Playground Session: https://api2.sourceacademy.nus.edu.sg/rees
const tree = value => left => right => list(value, left, right);
const not_defined = "N/A";
const top = tree => is_null(tree) ? null : head(tree);
const get_value = node => is_null(node) ? null : head(node);
const left = tree => is_null(tree) ? not_defined : head(tail(tree));
const right = tree => is_null(tree) ? not_defined : get_value(tail(tail(tree)));

// Tests
const a = tree(4)(list(5, 7))(6);
display(top(a));                // 4
display(left(a));               // [5, [7, null]]
display(top(left(a)));          // 5
display(right(a));              // 6
display(left(left(a)));         // 7
display(right(left(a)));        // null 
right(null);                    // "N/A" - Not applicable as right of null is not defined 

// ------------------------------------------------ //

// Tree balancing
function entry(tree) {
    return head(tree);
 }
 function left_branch(tree) {
    return head(tail(tree));
 }
 function right_branch(tree) {
    return head(tail(tail(tree)));
 }
 function make_tree(entry,left,right) {
    return list(entry,left,right);
 }
 function list_to_tree(elements) {
    return head(partial_tree(elements,length(elements)));
 }
 function partial_tree(elts, n) {
     if (n === 0) {
        return pair(null,elts);
     } else {
        const left_size = math_floor((n - 1) / 2);
        const left_result = partial_tree(elts, left_size);
        const left_tree = head(left_result);
        const non_left_elts = tail(left_result);
        const right_size = n - (left_size + 1);
        const this_entry = head(non_left_elts);
        const right_result = partial_tree(tail(non_left_elts),
                                          right_size);
        const right_tree = head(right_result);
        const remaining_elts = tail(right_result);
        return pair(make_tree(this_entry, 
                              left_tree, 
                              right_tree),
                    remaining_elts);
     }
 }
 
 list_to_tree(list(10, 20, 30));

// --------------------ROUGH---------------------------- //
 const tree = pair(pair(1, pair(2, null)), pair(3, pair(4, null)));
// slides
head(tree);         // top      // [1, [2, null]]
head(tail(tree));   // left     // 3? -- HOW is this left? -- looks like tree.right?
head(tail(tail(tree))); // right    // looks like tree.right.right?

// my understanding
// head(tree);         // [1, [2, null]]   
// head(head(tree));   // 1     // left?
head(tail(tree));       // 3    // right?
head(tail(tail(tree)));

function top(tree) { return head(tree);}
function left(tree) { return head(tail(tree));}
function right(tree) { return head(tail(tail(tree)));} // a bit weird, right?

function tree(value, left, right) {
  return list(value, left, right);
}