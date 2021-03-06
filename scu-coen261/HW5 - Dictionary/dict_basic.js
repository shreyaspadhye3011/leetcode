const key = head;
const value = tail;

const insert_dict = (item,dict) => pair(item, dict);

function build_dict(list) {
  return is_null(list) ? null : insert_dict(head(list), build_dict(tail(list)));
}

const lookup = dict => k => !is_null(dict) && 
                            (key(head(dict)) === k ? value(head(dict)) :
                                                     lookup(tail(dict))(k));

const update_dict = dict => (k, v) => {
  return is_null(dict) ? null 
  : key(head(dict)) === k
    ? insert_dict(pair(k, v), update_dict(tail(dict))(k, v)) 
    : insert_dict(head(dict), update_dict(tail(dict))(k, v));
};
                                                     
                                                     
const hungarian = build_dict(list(pair(1, "egy"), pair(2, "ketto"), pair(3, "harom"), pair(2, "lib")));

// hungarian;
// lookup(hungarian)(7);
update_dict(hungarian)(2, "milo");



// output of hungarian: (structure of a dictionary)
// [
//   [1, "egy"], [
//       [2, "ketto"], [
//           [3, "harom"], [
//               [2, "lib"], null
//           ]
//       ]
//   ]
// ]


// most likely output of hashset: (structure of a dictionary list)
// [
//   [1, [1, null]], 
//   [2, [2, null]], 
//   null
// ]

// [
//   [
//     [6, [6, null]], 
//     [5, [5, null]]
//   ], 
//   null
// ]

// const hungarian = build_dict(list(pair(1, list(2, 3)), pair(7, list(12, 13))));
// output: [[1, [2, [3, null]]], [[7, [12, [13, null]]], null]]
