// Todo: add is_null usage
function interleave_lists(first, second, interleaved) {
  // Todo: Always call with second as smaller
  if (first !== null && second !== null && array_length(second) > array_length(first)) { interleave_lists(second, first); }
  else {    
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
          interleaved = pair(interleaved, pair(head(first), head(second)));
        } else {
          interleaved = pair(head(first), pair(head(second), null));
        }
        interleave_lists(tail(first), tail(second), interleaved);
      }
  }
}


let result = interleave_lists(list(1,2,3), list(4,5,6), null);

let chck = pair(1, pair(2, null));
display(chck);
// for_each(x => display(x), result);