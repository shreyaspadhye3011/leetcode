// Basic fibonacci
// const fib = n => {
//   const fib_iter = n => a => b => count => {
//       return count === n ? b : fib_iter(n)(b)(a+b)(count+1);
//   };
//   return n < 1 ? "Not defined." : n === 1 ? 1 : fib_iter(n)(1)(2)(2);  
// };

// fib(0);

// Author: Shreyas Padhye, spadhye@scu.edu, 00001556287
// https://api2.sourceacademy.nus.edu.sg/evenfibsum

// returns sum of all even valued terms in the first n numbers of the fibonacci sequence
const fib_sum = n => {
  const is_even = num => num % 2 === 0;
  const fib_sum_iter = n => a => b => count => sum => {
    const updated_sum = is_even(b) ? sum + b : sum;
    return count === n || updated_sum === Infinity ? updated_sum : fib_sum_iter(n)(b)(a+b)(count+1)(updated_sum);
  };
  return n <= 1 ? 0 : fib_sum_iter(n)(1)(2)(2)(0);  
};

// tests
display(fib_sum(1));        // 0
display(fib_sum(2));        // 2
display(fib_sum(5));        // 10
display(fib_sum(7));        // 10
display(fib_sum(10));       // 44
fib_sum(4000000);           // Infinity

