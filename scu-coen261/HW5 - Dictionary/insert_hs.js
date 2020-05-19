const key = head;
const value = tail;

const hash = (value) => value % 31;

const lookup = dict => k => !is_null(dict) &&
                        	(key(head(dict)) === k ? value(head(dict)) :
                                             	   lookup(tail(dict))(k));

const contains_l = (set, x) => {
    // display(set);
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
     else { 
        //  return pair(append(dict, pair(k, pair(k, null))), null); 
         return insert_dict(k, pair(k, null))(dict);
     }
};

const insert_dict = (k, v) => dict => pair(pair(k, v), dict);

const update_dict = dict => (k, v) => {
  return is_null(dict) ? null 
  : key(head(dict)) === k
    ? insert_dict(k, v)(update_dict(tail(dict))(k, v))
    : insert_dict(key(head(dict)), value(head(dict)))(update_dict(tail(dict))(k, v));
};

const insert_hs = (set, x) => {
  const key = hash(x);
  const chain = lookup(set)(key);
  display(chain);
  if (chain === false) {
      return insert_chain_hs(key)(set);
  } else {
    //   display(x);
      const new_list = insert_l(x, chain);
      display("helo");
      display(new_list);
      return update_dict(set)(key, new_list);
  }
};

const a = insert_hs(null, 6);
display(a);
const b = insert_hs(a, 36);
display(b);
insert_hs(b, 37);









