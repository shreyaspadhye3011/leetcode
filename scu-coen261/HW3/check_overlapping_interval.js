function make_interval(x, y) { 
    return pair(x, y); 
}
function lower_bound(i) { 
    return head(i);
}
function upper_bound(i) { 
    return tail(i);
}
function print_interval(i) {
    return "[ "  + stringify(lower_bound(i)) + 
           " , " + stringify(upper_bound(i)) + " ]";
}
function add_interval(x, y) {
    return make_interval(lower_bound(x) + lower_bound(y),
                         upper_bound(x) + upper_bound(y));
}

// print_interval(add_interval(make_interval(1, 2), 
//                             make_interval(3, 5)));

function is_overlap() {
    
}

function check_overlapping_interval(array, i=0) {
    if (i > array_length(array)) { return false; }
    return is_overlap(array[i]) ? true : check_overlapping_interval(array, i+1);
}

// check_overlapping_interval(sor)

const sort = (arr) => {
    if (arr.length === 0) return [];
    const [curr, ...rest] = arr;
    const left = rest.filter(item => item <= curr);
    const right = rest.filter(item => item > curr);
    return sort(left)
      .concat([curr])
      .concat(sort(right));
  };

  console.log((sort([5, 2, 6, 3, 8, 1])));