// Todo: add is_null usage
function interleave_lists(first, second, interleaved) {
  // if both empty
  if (first === null && second === null) { return interleaved; }
  // first still has elements
  else if (second === null) { 
    interleaved = pair(interleaved, head(first)); 
    interleave_lists(tail(first), null, interleaved);
  }
  // if both still have elements, interleave
  else {
    if (interleaved === null) {
      interleaved = pair(head(first), pair(head(second), null));
    } else {
      interleaved = pair(interleaved, pair(head(first), head(second)));
    }
    display(interleaved);
    interleave_lists(tail(first), tail(second), interleaved);
  }
}

function interleave_lists_helper(first, second) {
    // always call interleave_lists with first array as larger
    if (array_length(first) >= array_length(second)) { 
        return interleave_lists(reverse(first), reverse(second), null); 
    } else {
        return interleave_lists(reverse(second), reverse(first), null); 
    }
}

let result = interleave_lists_helper(list(1,2,3), list(4,5,6));

let chck = pair(3, pair(1, pair(2, null)));
display(chck);
// for_each(x => display(x), result);