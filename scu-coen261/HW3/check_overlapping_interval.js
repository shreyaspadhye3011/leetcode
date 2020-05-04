function make_interval(x) { 
    return pair(x[0], x[1]); 
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



function check_overlapping_intervals(intervalOne, intervalTwo) {
    let inter1 = make_interval(intervalOne);
    let inter2 = make_interval(intervalTwo);
    // display(print_interval(inter1));
    // display(print_interval(inter2));
    return lower_bound(inter2) < upper_bound(inter1) || lower_bound(inter1) < upper_bound(inter2) ? true : false; 
    // return is_overlap(array[i]) ? true : check_overlapping_interval(array, i+1);
}

check_overlapping_intervals([1,3], [2,4]);

// print_interval(add_interval(make_interval(1, 2), 
//                             make_interval(3, 5)));

