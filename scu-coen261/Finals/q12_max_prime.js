// Author: Shreyas Padhye, spadhye@scu.edu, 00001556287

const remove_all = n => divisor => n % divisor !== 0 ? n : remove_all(math_floor(n/divisor))(divisor);

const get_max_prime_factor = n => current_divisor => max_prime => {
    return n === 0
    ? max_prime
    : current_divisor >= math_sqrt(n)
    ? n
    : n % current_divisor === 0 
    ? get_max_prime_factor(remove_all(n)(current_divisor))(current_divisor+1)(current_divisor)
    : get_max_prime_factor(n)(current_divisor+1)(max_prime);
};
// todo: use helper to pass init values
// todo: test for primes etc
get_max_prime_factor(15)(2)(2);     // 5
