// Basic fibonacci
// const fib = n => {
//   const fib_iter = n => a => b => count => {
//       return count === n ? b : fib_iter(n)(b)(a+b)(count+1);
//   };
//   return n < 1 ? "Not defined." : n === 1 ? 1 : fib_iter(n)(1)(2)(2);  
// };

// fib(0);


// return sum of all even valued terms in the first n numbers of the sequence
const fib_sum = n => {
  const is_even = num => num % 2 === 0;
  const fib_sum_iter = n => a => b => count => sum => {
    const updated_sum = is_even(b) ? sum + b : sum;
    return count === n ? updated_sum : fib_sum_iter(n)(b)(a+b)(count+1)(updated_sum);
  };
  return n <= 1 ? 0 : n === 2 ? 2 : fib_sum_iter(n)(1)(2)(2)(0);  
};

fib_sum(5);