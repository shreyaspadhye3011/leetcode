function foldr(op, init, xs) {
    return is_null(xs) ? init : op(head(xs), foldr(op, init, tail(xs))); }
  
  function length(xs) { return foldr((x, n) => n+1, 0, xs); }
  
  length([2, [3, [4, [4, null]]]]);