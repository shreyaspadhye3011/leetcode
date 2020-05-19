// Sol 1
const key = head;
const value = tail;

const insert_dict = (k, v) => dict => pair(pair(k, v), dict);

const build_dict = list => is_null(list) ? null :
          insert_dict(key(head(list)),value(head(list)))(build_dict(tail(list)));


const lookup = dict => k => !is_null(dict) && 
                            (key(head(dict)) === k ? value(head(dict)) :
                                                     lookup(tail(dict))(k));

const update_dict = dict => (k, v) => {
  return is_null(dict) ? null 
  : key(head(dict)) === k
    ? insert_dict(k, v)(update_dict(tail(dict))(k, v))
    : insert_dict(key(head(dict)), value(head(dict)))(update_dict(tail(dict))(k, v));
};
                                                     
                                                     
const hungarian = build_dict(list(pair(1, "egy"), pair(2, "ketto"), pair(3, "harom"), pair(2, "lib")));
display(update_dict(hungarian)(2, "milo"), "Sol 1:");


// SOl 2
const hash = (value) => value % 31;
const contains_l = (set, x) => {
  return !is_null(set) && (x === head(set)) || !is_null(set) && contains_l(tail(set), x); 
};

const insert_l = (x, set) => {
  return contains_l(set, x) ? set : pair(x, set);
};

const insert_chain_hs = k => dict => {
     if (is_null(dict)) { return pair(pair(k, pair(k, null)), null); }
     else { 
         return insert_dict(k, pair(k, null))(dict);
     }
};

const insert_hs = (set, x) => {
  const key = hash(x);
  const chain = lookup(set)(key);
  if (chain === false) {
      return insert_chain_hs(key)(set);
  } else {
      const new_list = insert_l(x, chain);
      return update_dict(set)(key, new_list);
  }
};

const a = insert_hs(null, 6);
// display(a);          // output: [[6, [6, null]], null]
const b = insert_hs(a, 36);
// display(b);          // output: [[5, [5, null]], [[6, [6, null]], null]]
display(insert_hs(b, 37), "Sol 2:");   // Final output: [[5, [5, null]], [[6, [37, [6, null]]], null]]
