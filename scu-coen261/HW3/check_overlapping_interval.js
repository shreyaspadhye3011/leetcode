// Session: https://source-academy.github.io/playground#chap=4&exec=1000&ext=NONE&prgrm=GYVwdgxgLglg9mABAWwIYGsCmB9GYqYBOAbqgDYAUAHgJSIDeiAUIq4oZlCIUgA6oxC1ANoAGALoAaRFWEBGcTQDczAL5NQkWAkRk4AdyLYARnHAATCjDqMWbDlx6IAFplSXrSpus3R4SEF5eI1MLKxtmNnZObiQoAUpPbyYNcD8dCFcIdGw4YiIyVCC8AHNcfCJSMgBnKwqScgB5MExpPAIGsgAVfTgbO1YyTkR2ojlEAF4UDBxRzrqOqubMZQHdYbmAJknprHLF8gXK8h6%2BryiHWN0DELMwD3q5OgAea8NCEzuHjs26NYB%2BRAUPTvT5hLYvRCBYIfUL3I6EJ6IQFQQggTCIABciGA5GqKzW2OBN1hXwRSNe0Nu4Pqv2RiFR6KxOLxKxUySYAHpOYhMphsrl8oRCsUwGU5lVavJNpI5ABmKSIMSSAAsihU3JZNUwXJ5fIFeQKRV4pX2xxqFGVauk0tlCuUiE1uO1ut5WRyhuFxtNErxltEqsV8jt6tYmsZOv1HqFIpNYrNnSlckDNpl9pUUXDaJ1TCAA&variant=default

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
    ? (lower_bound(inter2) < upper_bound(inter1) ? true : false)
    : (lower_bound(inter1) < upper_bound(inter2) ? true : false); 
}

// check_overlapping_intervals([12,13], [0,4]); // false
// check_overlapping_intervals([0,4], [12,13]); // false
// check_overlapping_intervals([0,4], [1,13]);  // true
check_overlapping_intervals([1,4], [2,3]);     // true

