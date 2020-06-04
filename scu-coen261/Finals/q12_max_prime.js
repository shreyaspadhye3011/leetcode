// Author: Shreyas Padhye, spadhye@scu.edu, 00001556287
// sourceacademy: https://api2.sourceacademy.nus.edu.sg/largestprimefactor

// keep dividing a given number with a divisor until it can
const remove_all = n => divisor => n % divisor !== 0 ? n : remove_all(math_floor(n/divisor))(divisor);

// retrieve largest prime factor for a number
const get_max_prime_factor = n => current_divisor => max_prime => {
    return n === 0
    ? max_prime
    : current_divisor >= math_sqrt(n)
    ? n
    : n % current_divisor === 0 
    ? get_max_prime_factor(remove_all(n)(current_divisor))(current_divisor+1)(current_divisor)
    : get_max_prime_factor(n)(current_divisor+1)(max_prime);
};

const max_prime_factor = n => get_max_prime_factor(n)(2)(2);

max_prime_factor(600851475143);     // 6857
