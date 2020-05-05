// Todo: add is_null usage
function interleave_lists(first, second, interleaved) {
  // if both empty
  // display(interleaved);
  if (first === null && second === null) { 
      return interleaved; 
  }
  // first still has elements
  else if (second === null) { 
  //   interleaved = pair(head(first), interleaved); 
     interleaved = append(interleaved, pair(head(first), null));
    return interleave_lists(tail(first), null, interleaved);
  }
  // if both still have elements, interleave
  else {
    if (interleaved === null) {
      interleaved = pair(head(first), pair(head(second), null));
      // display(tail(first));
      // display(tail(second));
    } else {
      // interleaved = pair(head(first), pair(head(second), interleaved));
      // display(head(first));
      // display(interleaved);
      // display("oh");
      interleaved = append(interleaved, pair(head(first), pair(head(second), null)));
      // display(append(interleaved, head(first)));
      // interleaved = append(interleaved, head(second));
    }
    return interleave_lists(tail(first), tail(second), interleaved);
  }
  }
  
  function interleave_lists_helper(first, second) {
  //   let result = [];
    // always call interleave_lists with first array as larger
    if (length(first) >= length(second)) { 
          return interleave_lists(first, second, null); 
      //   return result;
    } else {
        return interleave_lists(second, first, null); 
      //   return result;
    }
  }
  
  interleave_lists_helper(list(1,2,3), list(4,5,6,7,8));
  
  // append(list(1, 4), 3);
  
  // append([1, [4, null]],2);
  // append([1, [4, 2]], pair(5,7));
  
  // let chck = pair(3, pair(1, pair(2, null)));
  // display(chck);
  // for_each(x => display(x), result);