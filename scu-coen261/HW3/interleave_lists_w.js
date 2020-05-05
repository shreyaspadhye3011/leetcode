// Todo: add is_null usage
function interleave_lists(first, second, interleaved) {
  // if both empty
  if (first === null && second === null) { 
      return interleaved; 
  }
  // first still has elements
  else if (second === null) { 
    interleaved = append(interleaved, pair(head(first), null));
    return interleave_lists(tail(first), null, interleaved);
  }
  // if both still have elements, interleave
  else {
    if (interleaved === null) {
      interleaved = pair(head(first), pair(head(second), null));
    } else {
      interleaved = append(interleaved, pair(head(first), pair(head(second), null)));
    }
    return interleave_lists(tail(first), tail(second), interleaved);
  }
  }
  
  function interleave_lists_helper(first, second) {
    // always call interleave_lists with first array as larger
    if (length(first) >= length(second)) { 
      return interleave_lists(first, second, null); 
    } else {
      return interleave_lists(second, first, null); 
    }
  }
  
  interleave_lists_helper(list(1,2,3), list(4,5,6));
  interleave_lists_helper(list(1,2,3,7,8), list(4,5,6));