// Author: Shreyas Padhye, spadhye@scu.edu, 00001556287
// sourceacademy: https://api2.sourceacademy.nus.edu.sg/lcm

// get lcm of two numbers
const lcm = a => b => a >= b ? lcm_helper(a)(b)(1) : lcm_helper(b)(a)(1);
const is_divisible = a => b => a % b === 0;
const lcm_helper = a => b => multiplier => is_divisible(a*multiplier)(b) 
                                            ? a*multiplier : lcm_helper(a)(b)(multiplier+1);
                                            

// any number that is divisible by these will definitely be divisible by 1-10. Hence only these considered in calculation
const number_list = list(20, 19, 18, 17, 16, 15, 14, 13, 12, 11);
const get_value = xs => is_null(xs) ? null : head(xs);
const next = xs => is_null(xs) ? null : tail(xs);
const find_lcm = xs => current_lcm => is_null(next(xs))
                                        ? current_lcm
                                        : find_lcm(next(xs))(lcm(current_lcm)(get_value(next(xs))));
                                        

const get_lcm = mun_list => find_lcm(mun_list)(20);
get_lcm(number_list);      // 232792560