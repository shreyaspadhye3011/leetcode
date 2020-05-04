// Source specific code
// https://source-academy.github.io/playground#chap=4&prgrm=GYVwdgxgLglg9mABAWwIYGsCmB9GYqYBOAbqgDYAUAHgDSICeAlIgN6IBQiXihmUIhJAAdUMQtTpMA3BwC+7UJFgJEZOAHci2AEZxwAEwoxmbTt179BiABaZUh41PbzF0eEhBChW3QaMmObh4+ASQoUUpHZwVwNxUhQjwoXHwiUkiTMy4LUMQAIgBtfK4AakQAZyhEsABzGGB6CjVNQh09MAdGZjKsoKC8xDoBssrquoaKT29W3w7-buKAXTynF1jlJHt9FIIScgkGTKCcqzQsHbT95p92wyoF65nbiiYaXr6Pz+4pm797xDKPyefiYjFW7HYCSSFz2lC2MPSFDOOCSl0oAEY6AAmRh0d5fAkfZEI-YAZjoAFYumCgA
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

print_interval(add_interval(make_interval(1, 2), 
                            make_interval(3, 5)));