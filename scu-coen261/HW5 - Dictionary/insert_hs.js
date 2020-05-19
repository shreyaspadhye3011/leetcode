const key = head;
const value = tail;

const hash = (value) => value % 31;

const lookup = dict => k => !is_null(dict) &&
                        	(key(head(dict)) === k ? value(head(dict)) :
                                             	   lookup(tail(dict))(k));

const contains_l = (set, x) => {
  return !is_null(set) && x === head(set) || contains_l(tail(set), x); 
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

const insert_chain_hs = (k, v) => dict => pair(pair(k, list()), dict);

const insert_hs = (set, x) => {
  const key = hash(x);
  const chain = lookup(set)(key);
  if (is_null(chain)) {
      insert_chain_hs(key, set);
  } else {
      insert_l(x, chain);
  }
};







