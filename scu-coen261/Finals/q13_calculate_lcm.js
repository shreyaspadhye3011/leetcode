// 232,792,560

// xs - 20, 19, 18, 17, 16, 15, 14, 13, 12, 11

// for every pair of numbers from back, get lcm(head(xs), head(tail(xs))) and pass it ahead into the list

const lcm = a => b => a >= b ? lcm_helper(a)(b)(1) : lcm_helper(b)(a)(1);
const is_divisible = a => b => a % b === 0;
const lcm_helper = a => b => multiplier => is_divisible(a*multiplier)(b) 
                                            ? a*multiplier : lcm_helper(a)(b)(multiplier+1);
                                            

// todo: create this list dynamically
// any number that is divisible by these will definitely be divisible by 1-10
const number_list = list(20, 19, 18, 17, 16, 15, 14, 13, 12, 11);
number_list;
head(number_list);  // 20
tail(number_list);  // [19, [18, [17, [16, [15, [14, [13, [12, [11, null]]]]]]]]]
