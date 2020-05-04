// Todo: add is_null usage
function interleave_lists(first, second, interleaved) {
  // if both empty
  if (first === null && second === null) { 
      return interleaved; 
  }
  // first still has elements
  else if (second === null) { 
    interleaved = pair(head(first), interleaved); 
    return interleave_lists(tail(first), null, interleaved);
  }
  // if both still have elements, interleave
  else {
    if (interleaved === null) {
      interleaved = pair(head(first), pair(head(second), null));
    } else {
      interleaved = pair(head(first), pair(head(second), interleaved));
    }
    return interleave_lists(tail(first), tail(second), interleaved);
  }
}

function interleave_lists_helper(first, second) {
    let result = [];
    // always call interleave_lists with first array as larger
    if (array_length(first) >= array_length(second)) { 
         result = interleave_lists(reverse(first), reverse(second), null); 
         return result;
    } else {
        result = interleave_lists(reverse(second), reverse(first), null); 
        return result;
    }
}

interleave_lists_helper(list(1,2,3,7), list(4,5,6));

// let chck = pair(3, pair(1, pair(2, null)));
// display(chck);
// for_each(x => display(x), result);