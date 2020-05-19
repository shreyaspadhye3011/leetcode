const key = head;
const value = tail;

const hash = (value) => value % 31;

const lookup = dict => k => !is_null(dict) &&
                        	(key(head(dict)) === k ? value(head(dict)) :
                                             	   lookup(tail(dict))(k));

const contains_l = (set, x) => {
    display(set);
  return !is_null(set) && (x === head(set)) || !is_null(set) && contains_l(tail(set), x); 
};

const insert_l = (x, set) => {
  return contains_l(set, x) ? set : pair(x, set);
};

const contains_hs = (hashset, x) => {
  if (is_null(hashset)) { return false; } else {}
  const key = hash(x);
  const chain = lookup(hashset)(key);
  return !is_null(chain) && contains_l(chain, x);
};

const insert_chain_hs = k => dict => {
     if (is_null(dict)) { return pair(pair(k, pair(k, null)), null); }
     else { return append(dict, pair(k, pair(k, null))); }
};

const insert_hs = (set, x) => {
  const key = hash(x);
  const chain = lookup(set)(key);
//   display(chain);
  if (chain === false) {
      return insert_chain_hs(key)(set);
  } else {
    //   display(x);
      return insert_l(x, chain);
  }
};

const a = insert_hs(null, 6);   
display(a);         // [[6, [6, null]], null]
const b = insert_hs(a, 36);
display(b);         // [[6, [6, null]], [5, [5, null]]]
insert_hs(b, 37);   // [37, [6, null]] (all good just need to update list at key 6 with this value)









