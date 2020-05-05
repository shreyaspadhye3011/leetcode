// for_each 
for_each(x => display(x), 
         list(57, 321, 88));

// list creation - 1
let chck = pair(3, pair(1, pair(2, null)));     // [3, [1, [2, null]]]
display(chck);

// list creation - 2
list(1,2,3);      // [1, [2, [3, null]]]

// list append
append([1, [4, null]],pair(2, null));   // [1, [4, [2, null]]]