// Author: Shreyas Padhye, spadhye@scu.edu, 00001556287
// Courtesy: Prof. Vlad Patryshev & SICP JS
function contains_sl(set, x) {
    return !is_null(set) && (x === head(set) ||
      (x >= head(set) && contains_sl(tail(set), x))); // bug!!!
  }
  function insert_sl(set, x) {
    return contains_sl(set, x) ? set : is_null(set) || x < head(set) ? pair(x, set)
                                     : pair(head(set), insert_sl(tail(set), x)); // bug!!!
  }
  
  const l = list();
  insert_sl(insert_sl(insert_sl(insert_sl(l, 99), 90), 95), 99);  // [90, [95, [99, null]]]
  // seems to be working. need to find bug