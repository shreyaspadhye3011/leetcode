// Playground Session: https://tinyurl.com/ycnny6o7

function make_interval(x) { 
    return pair(x[0], x[1]); 
}
function lower_bound(i) { 
    return head(i);
}
function upper_bound(i) { 
    return tail(i);
}

function check_overlapping_intervals(intervalOne, intervalTwo) {
    let inter1 = make_interval(intervalOne);
    let inter2 = make_interval(intervalTwo);
    return lower_bound(inter1) < lower_bound(inter2) 
    ? lower_bound(inter2) < upper_bound(inter1) 
    : lower_bound(inter1) < upper_bound(inter2); 
}

// check_overlapping_intervals([12,13], [0,4]); // false
// check_overlapping_intervals([0,4], [12,13]); // false
// check_overlapping_intervals([0,4], [1,13]);  // true
check_overlapping_intervals([1,4], [2,3]);     // true

