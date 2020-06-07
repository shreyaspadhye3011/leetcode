// Author: Shreyas Padhye, spadhye@scu.edu, 00001556287
// sourceacademy: https://api2.sourceacademy.nus.edu.sg/evenfibonaccisum 

// returns sum of all even valued terms in the first n numbers of the fibonacci sequence
const fib_sum = n => {
  const is_even = num => num % 2 === 0;
  const fib_sum_iter = n => a => b => count => sum => {
    const updated_sum = is_even(b) ? sum + b : sum;
    return b < n ? fib_sum_iter(n)(b)(a+b)(count+1)(updated_sum) : sum;
  };
  return fib_sum_iter(n)(1)(2)(2)(0);  
};

// tests
fib_sum(4000000);           // 4613732







// Basic fibonacci
// const fib = n => {
//   const fib_iter = n => a => b => count => {
//       return count === n ? b : fib_iter(n)(b)(a+b)(count+1);
//   };
//   return n < 1 ? "Not defined." : n === 1 ? 1 : fib_iter(n)(1)(2)(2);  
// };

// fib(0);




